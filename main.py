import sys
import os
import time
from fastapi import FastAPI, Request
import asyncio
import pyatv

os.environ['TZ'] = 'Europe/Berlin'
time.tzset()

app = FastAPI(
    title="vestaboard-control",
    description="foobar")

@app.get("/")
async def init():
#    return {"Hello": "FPP"}
    results = await pyatv.scan(loop=asyncio.get_event_loop())
    output = "\n\n".join(str(result) for result in results)
    return {"Hello": output}
