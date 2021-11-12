import json
import requests
import os

url = "localhost:8443"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiI4NDRlMjUxYi01NzRiLTQ2ZTYtOTI0Ny1mNzZmMWY3MGE2MzciLCJpc3MiOiJhdXRodmVydHguaXVkeC5pbyIsImF1ZCI6ImNhdGFsb2d1ZS5pdWR4LmlvIiwiZXhwIjoxNjMyMjYxMjkxLCJpYXQiOjE2MzIyMTgwOTEsImlpZCI6InJpOmlpc2MuYWMuaW4vODlhMzYyNzNkNzdkYWM0Y2YzODExNGZjYTFiYmU2NDM5MjU0N2Y4Ni9jYXRhbG9ndWUuaXVkeC5pby9jYXRhbG9ndWUvY3J1ZCIsInJvbGUiOiJwcm92aWRlciIsImNvbnMiOnt9fQ.BTNDXRQ90C9wTWGtcYzIgjZgbhoV_ELX6smaJxjbvceKFHbVaHMaxYMMyyTrQUGe3b7BpGgODu4vR6JAycfmRg"

api = "http://" + url + "/iudx/cat/v1/item"

headers = {"instance": "pune", "content-type": "application/json", "token": token}


resource_item = {}

with open("./aqm/rg.json", "r") as f:
    resource_item = json.load(f)

r = requests.post(api, json.dumps(resource_item), headers=headers, verify=False)
print(r.status_code)
print(r.json())
