import json
import requests
import os

url = "api.k8s-catalogue.iudx.io"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiI4NDRlMjUxYi01NzRiLTQ2ZTYtOTI0Ny1mNzZmMWY3MGE2MzciLCJpc3MiOiJhdXRodmVydHguaXVkeC5pbyIsImF1ZCI6ImNhdGFsb2d1ZS5pdWR4LmlvIiwiZXhwIjoxNjMyMjYxMjkxLCJpYXQiOjE2MzIyMTgwOTEsImlpZCI6InJpOmlpc2MuYWMuaW4vODlhMzYyNzNkNzdkYWM0Y2YzODExNGZjYTFiYmU2NDM5MjU0N2Y4Ni9jYXRhbG9ndWUuaXVkeC5pby9jYXRhbG9ndWUvY3J1ZCIsInJvbGUiOiJwcm92aWRlciIsImNvbnMiOnt9fQ.BTNDXRQ90C9wTWGtcYzIgjZgbhoV_ELX6smaJxjbvceKFHbVaHMaxYMMyyTrQUGe3b7BpGgODu4vR6JAycfmRg"

api = "https://" + url + "/iudx/cat/v1/item"

headers = {"content-type": "application/json", "token": token}


id_to_delete = "iisc.ac.in/89a36273d77dac4cf38114fca1bbe64392547f86/rs.iudx.io/pune-env-flood-2"


r = requests.delete(api+"?id="+id_to_delete, headers=headers, verify=False)
print(r.status_code)
