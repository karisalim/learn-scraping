import requests
from bs4 import BeautifulSoup

URL = "https://www.thewhiskyexchange.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (BeOS; U; Haiku BePC; en-US; rv:1.8.1.17) Gecko/20080831 BonEcho/2.0.0.17"
}

r = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky', headers=headers)