import pandas as pd
import requests
from html import unescape
from constants import *
from wrikeFunctions import *
from slackFunctions import *
from threading import Thread
from fastapi import FastAPI, Request
from typing import Any


app = FastAPI()


@app.post("/wrike-webhook")
async def wrike_webhook(request: Request):
    # Obtener el body como diccionario
    payload = await request.json()  # ⚠ Esto devuelve un dict SOLO si el body es JSON
    print("Evento recibido desde Wrike:", payload)

    # Aquí pones tu lógica, por ejemplo mandar mensaje a Slack
    # requests.post(...)

    return {"status": "ok"}

    




# response = requests.post(f"{BASE_URL_SLACK}chat.postMessage", headers=HEADERS_SLACK, verify=SSL, json={
#     "channel": "#espacio-pureba",
#     "text": "Hola desde mi script"
# })


