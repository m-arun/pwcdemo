import json
import requests
import os

url = "http://localhost:9999"
token = ""


api = url + "/iudx/cat/v1/item"
headers = {"content-type": "application/json", "token": token}


# Push any document

def push(doc):
    r = requests.post(api, json.dumps(doc), headers=headers, verify=False)
    print(r.status_code)
    print(r.json())
    if (r.status_code == 201):
        print("Successfully pushed")




# Insert provider item first
with open("./provider.json", "r") as f:
    provider = json.load(f)
    push(provider)

# Insert Resource Server
with open("./rs.json", "r") as f:
    server = json.load(f)
    push(server)

# Insert Resource Group
with open("./rg.json", "r") as f:
    group = json.load(f)
    push(group)

# Insert Resources
with open("./ri.json", "r") as f:
    resources = json.load(f)
    for resource in resources:
        push(resource)
