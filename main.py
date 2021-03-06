#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests

reader = SimpleMFRC522()


def detected(id):
    body={
        "id":id
    }
    r = requests.post("http://localhost:5000/rfid", 
                json=body, 
                headers={"content-type":"application/json"})

try:
    while(True):
            id, text = reader.read()
            print(id)
            print(text)
            detected(id)

finally:
    GPIO.cleanup()
