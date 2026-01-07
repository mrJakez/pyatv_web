# Scan

Get details for all AppleTV devices within the same network.

**URL** : `/scan/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

## Success Response

**Code** : `200 OK`

**Content examples**

This is a regular example for a scan within a home network:

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
