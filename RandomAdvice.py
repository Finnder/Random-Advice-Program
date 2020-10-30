import requests
import json
import time

AllAdvice = []

def parse(link):
    jsonlink = requests.get(link)
    parseinfo = jsonlink.json()
    return parseinfo

while True:
    time.sleep(1.8)
    advice = parse('https://api.adviceslip.com/advice')
    print("--> " + advice['slip']['advice'])
    AllAdvice.append(advice['slip']['advice'])
