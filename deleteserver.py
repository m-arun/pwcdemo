import json
import requests
import os

url = "cattest.iudx.io"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiI4NDRlMjUxYi01NzRiLTQ2ZTYtOTI0Ny1mNzZmMWY3MGE2MzciLCJpc3MiOiJhdXRodmVydHguaXVkeC5pbyIsImF1ZCI6ImNhdGFsb2d1ZS5pdWR4LmlvIiwiZXhwIjoxNjMxODk0MTMzLCJpYXQiOjE2MzE4NTA5MzMsImlpZCI6InJzOmNhdGFsb2d1ZS5pdWR4LmlvIiwicm9sZSI6ImFkbWluIiwiY29ucyI6e319.Q3R8NPpy6Kdvcxhk_NhBX8KICDK5M2zEgHKBvFpBMeutZUFL-5JTxfdT0Qx5Yq6ETSjW2g9F-OEHJRlpedsJtw"

api = "https://" + url + "/iudx/cat/v1/instance?id=datakaveri.org/f7e044eee8122b5c87dce6e7ad64f3266afa41dc/rs.iudx.io"

headers = {"content-type": "application/json", "token": token}


resource_item = {}


r = requests.delete(api, headers=headers, verify=False)
print(r.status_code)
print(r.json())
