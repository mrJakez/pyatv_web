import sys
import os
import time
from fastapi import FastAPI, Request, HTTPException
import asyncio
import pyatv
from pyatv.storage.file_storage import FileStorage

# PAIRING:
# To connect use the pairning function of "atvremote wizard". Next copy  or mount the
# .pyatv.conf file from the current user into the root dir of the python app.

os.environ['TZ'] = 'Europe/Berlin'
time.tzset()

app = FastAPI(
    title="vestaboard-control",
    description="foobar")


async def get_atv(givenId):
    """Add credentials to pyatv device configuration."""

    connect: bool = False
    if not hasattr(app.state, 'devices'):
        app.state.devices = {}
        connect = True
    elif not givenId in app.state.devices:
        connect = True

    if connect:
        loop = asyncio.get_event_loop()

        results = await pyatv.scan(identifier=givenId, loop=loop)
        if not results:
            raise HTTPException(status_code=404, detail="Device not found")

        try:
            # Load the same storage that pyatv uses internally (e.g. in atvremote)
            storage = FileStorage('.pyatv.conf', loop)
            await storage.load()
            atv = await pyatv.connect(results[0], loop=loop, storage=storage)
        except Exception as ex:
            raise HTTPException(status_code=500, detail=f"Failed to connect to device: {ex}")

        if not hasattr(app.state, 'devices'):
            app.state.devices = {}

        app.state.devices[givenId] = atv

    return app.state.devices[givenId]


@app.get("/scan")
async def scan():
    devices = []
    for result in await pyatv.scan(loop=asyncio.get_event_loop()):
        devices.append({
            "name": result.name,
            "identifier": result.identifier,
            "address": str(result.address)
        })

    return {"devices": devices}


@app.get("/playing/{givenId}")
async def playing(givenId):
    try:
        atv = await get_atv(givenId)
        playing = await atv.metadata.playing()
        #artwork = await atv.metadata.artwork()

    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Remote control command failed: {ex}")

    return {"status": playing}


@app.get("/set_position/{givenId}/{position}")
async def playing(givenId, position):
    try:
        atv = await get_atv(givenId)
        rc = atv.remote_control
        await rc.set_position(int(position))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Remote control command failed: {ex}")

    return {"status": "ok"}


@app.get("/current_app/{givenId}")
async def playing(givenId):
    try:
        atv = await get_atv(givenId)
        currentApp = atv.metadata.app

    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Remote control command failed: {ex}")

    return {
        "name": currentApp.name,
        "identifier": currentApp.identifier,
    }