import requests
from constants import *
from html import unescape
import json
import time
import urllib.parse

def getSlackAccessToken():
    clientId = "9003719705777.9314792416134"
    clientSecret = "ff1ddda5dea409c69e31a95549fb16d2"
    redirectURL = "https://localhost:8000/callback"
    scope = "channels:read chat:write users:read"

    params = {
        "client_id": clientId,
        "scope": scope,
        "redirect_uri": redirectURL,
    }
    
    url = "https://slack.com/oauth/v2/authorize?" + urllib.parse.urlencode(params)
    print("Visita esta URL para autorizar la app:", url)

