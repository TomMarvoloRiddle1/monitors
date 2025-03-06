import os
from dotenv import load_dotenv
load_dotenv()
from proxyLess import FE_5090
from proxyMode import FE_5090proxy


if os.getenv('proxymode').upper() == "ON":
    FE_5090proxy(start=input("T to start, F to exit"))
else:
    FE_5090(start=input("T to start, F to exit"))
