from pydoc import cli
from twilio_creds import AUTH_TOKEN, SID, PHONE_NUM
from twilio.rest import Client
import sys

RCV_NUM = ""

try:
    RCV_NUM = sys.argv[1]
except:
    RCV_NUM = "+18175830095"


client = Client(SID, AUTH_TOKEN)

message = client.messages.create(
    body="sus.",
    from_=PHONE_NUM,
    to=RCV_NUM
)