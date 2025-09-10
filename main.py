import base64
import configparser
import os

import bs4
import requests
from pydbus import SystemBus

configfile = f"{os.path.realpath(os.path.dirname(__file__))}/config.ini"
if not os.path.isfile(configfile):
    print(f"{configfile} not found")
    exit(1)
config = configparser.ConfigParser()
config.read(configfile)
if "signal" not in config or "number" not in config["signal"]:
    print(f"number not found in {configfile}")
    exit(1)
if "signal" not in config or "group" not in config["signal"]:
    print(f"group not found in {configfile}")
    exit(1)

bus = SystemBus()
signal = bus.get('org.asamk.Signal', object_path=f'/org/asamk/Signal/_{config["signal"]["number"]}')

response = requests.get("https://www.opendoors.de/aktiv-werden/beten/taegliche-gebetsanliegen")
if response.status_code != 200:
    print("prayer requests could not be fetched")
    exit(1)

html = response.text
soup = bs4.BeautifulSoup(html, 'html.parser')
prayer_request_div = soup.find("div", class_="view-daily-prayer-request")
country = prayer_request_div.find("div", class_="views-field-field-country").text.strip()
body = prayer_request_div.find("div", class_="views-field-body").text.strip()

signal.sendGroupMessage(f"""{country}:

{body}""", [], base64.b64decode(config["signal"]["group"].strip()))
