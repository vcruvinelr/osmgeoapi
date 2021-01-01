from typing import Optional
from fastapi import FastAPI
import requests 
import urllib
import json

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/points")
async def read_data():
    url = 'https://overpass-api.de/api/interpreter?data=%2F*%0AThis+has+been+generated+by+the+overpass-turbo+wizard.%0AThe+original+search+was%3A%0A%E2%80%9C%22Drinking+Water%22%E2%80%9D%0A*%2F%0A%5Bout%3Ajson%5D%5Btimeout%3A25%5D%3B%0A%2F%2F+gather+results%0A(%0A++%2F%2F+query+part+for%3A+%E2%80%9C%22Drinking+Water%22%E2%80%9D%0A++node%5B%22amenity%22%3D%22drinking_water%22%5D(41.888093552297626%2C12.489877939224241%2C41.89473047541447%2C12.496658563613892)%3B%0A)%3B%0A%2F%2F+print+results%0Aout+body%3B%0A%3E%3B%0Aout+skel+qt%3B'
    resp = urllib.request.urlopen(url).read()
    output = json.loads(resp)
    return output