from fastapi import FastAPI
from typing import Optional
import aiohttp
app = FastAPI()

@app.get('/o/{url0}/{url1}')
async def oauth(url0: str, url1: str, code):
  session = aiohttp.ClientSession()
  if (url0 == 'luxor'):
    if (url1 == 'discord'):
      typeofauth = '11'
      CLIENT_SECRET = 'BI-qAAaGp56osoRH7qv1RFcJxtwgqOl9'
      REDIRECT_URI = 'https://auth.voltadigital.io'
    
      data = {
        'client_id': 973336133972926504,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
      }
      headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
      async with session.post('https://discord.com/api/v8/oauth2/token', headers=headers, json=data):
          data = await r.json
      return data