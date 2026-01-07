# pyatv_web
FastAPI webserver wrapper for pyatv. Therefore it can easily be integrated into a docker based eco system.

## RESTful endpoints
### Initialization related

To initialize a client we need the corresponding AppleTV identifier. Therefore a dedicated endpoint is given:

* [Scan ](services/scan.md) : `GET /scan/`

### Change position related

Endpoints for manipulating the current play position. They are required to implement home automation features like rewinding a movie if someone has left the livingrom to grap a drink in the kitchen etc.

* [Currently Playing](services/playing.md) : `GET /playing/{givenId}`
* [Set a specific position](services/set_position.md) : `GET /set_position/{givenId}/{position}`
* [Current app](services/current_app.md) : `GET /current_app/{givenId}`

# CheatSheet for atv within the container

```console
atvremote scan
```
