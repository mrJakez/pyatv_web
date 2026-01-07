# Scan

Get details for all AppleTV devices within the same network.

**URL** : `/scan/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

## Success Response

**Code** : `200 OK`

**Content examples**

For a User with ID 1234 on the local database where that User has saved an
email address and name information.

```json
{
  "devices": [
    {
      "name": "Wohnzimmer",
      "identifier": "76:44:05:48:8C:58",
      "address": "10.10.10.141"
    },
    {
      "name": "Schlafzimmer",
      "identifier": "42:97:D3:AA:A4:9D",
      "address": "10.10.10.103"
    },
    {
      "name": "Büro",
      "identifier": "80:4A:F2:98:17:34",
      "address": "10.10.10.97"
    }
  ]
}
```
