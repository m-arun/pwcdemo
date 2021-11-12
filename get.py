import json
import requests
import os


gid = "varanasismartcity.gov.in/62d1f729edd3d2a1a090cb1c6c89356296963d55/rs.iudx.org.in/varanasi-env-aqm"
rid = "varanasismartcity.gov.in/62d1f729edd3d2a1a090cb1c6c89356296963d55/rs.iudx.org.in/varanasi-env-aqm"


old_prefix = "varanasismartcity.gov.in/62d1f729edd3d2a1a090cb1c6c89356296963d55"
new_prefix = "iisc.ac.in/89a36273d77dac4cf38114fca1bbe64392547f86"

url = "api.catalogue.iudx.org.in"


out = "./aqm/"


api_rg = "https://" + url + "/iudx/cat/v1/item?id=" + gid
api_ri = "https://" + url + "/iudx/cat/v1/relationship?id=" + rid + "&rel=resource"

d = json.dumps(requests.get(api_rg).json()["results"][0], indent=4).replace(old_prefix, new_prefix).replace("rs.iudx.org.in", "rs.iudx.io").replace("datakaveri.org/27e503da0bdda6efae3a52b3ef423c1f9005657a", "datakaveri.org/f7e044eee8122b5c87dce6e7ad64f3266afa41dc/rs.iudx.io") 
with open(out + "rg.json", "w") as f:
    f.write(d)


d = json.dumps(requests.get(api_ri).json()["results"], indent=4).replace(old_prefix, new_prefix).replace("rs.iudx.org.in", "rs.iudx.io").replace("datakaveri.org/27e503da0bdda6efae3a52b3ef423c1f9005657a", "datakaveri.org/f7e044eee8122b5c87dce6e7ad64f3266afa41dc/rs.iudx.io") 
with open(out + "ri.json", "w") as f:
    f.write(d)
