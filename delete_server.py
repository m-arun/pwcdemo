import json
import requests
import os

url = "cattest.iudx.io"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiIzZjA4ZTFiYS1mNGMwLTRlZDAtODZkYS1lZGY3MDkyZDYzMzMiLCJpc3MiOiJhdXRodmVydHguaXVkeC5pbyIsImF1ZCI6ImNhdGFsb2d1ZS5pdWR4LmlvIiwiZXhwIjoxNjM2NTE1ODUyLCJpYXQiOjE2MzY0NzI2NTIsImlpZCI6InJpOmRhdGFrYXZlcmkub3JnL2Y3ZTA0NGVlZTgxMjJiNWM4N2RjZTZlN2FkNjRmMzI2NmFmYTQxZGMvY2F0YWxvZ3VlLml1ZHguaW8vY2F0YWxvZ3VlL2NydWQiLCJyb2xlIjoicHJvdmlkZXIiLCJjb25zIjp7fX0.7oleCKNhAl4JhX1J89PWFO9fWPK-1X56o48sC6VvoC8FuCb7ozKq3OCpp7JZzmWZFiUsq59zj57Zk3GjSuOMlA"

api = "https://" + url + "/iudx/cat/v1/item?id=datakaveri.org/f7e044eee8122b5c87dce6e7ad64f3266afa41dc/rs.iudx.io"

headers = {"content-type": "application/json", "token": token}


resource_item = {}

r = requests.delete(api, headers=headers, verify=False)
print(r.status_code)
print(r.json())
