import requests
from getpass import getpass
import json

username = 'alexsoshnikov'

r = requests.get('https://raw.githubusercontent.com/evgeniy-trebin/moscow-metro/master/stations-time.json',
                 auth=(username, 'g9sN2PCe3CTWdiS'))


obj = json.loads(r.text)
print(obj[0]['links'])
