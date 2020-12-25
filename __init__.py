import requests
import random
from lxml import etree
import json
from helpers import get_email, get_phone

class ScrapInsta():
    def __init__(self):
        user_agent = random.choice([ 
            "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.600.0 Safari/534.14", 
            "Mozilla/5.0 (X11; U; Windows NT 6; en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.587.0 Safari/534.12", 
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13", 
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16", 
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20", 
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1", 
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2", 
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7", 
            "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11", 
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19"])
        self.session = requests.Session()
        self.session.headers = {"User-Agent": user_agent}
        

    def scrape_data(self, username):
        attributes = {}
        url = "https://www.instagram.com/{}/"
        response = self.session.get(url.format(username))
        response.raise_for_status()
        if response.ok:
            root = etree.HTML(response.content)
            raw_data = root.xpath("//script[contains(text(), 'entry_data')]")[0].text
            raw_data = raw_data[raw_data.find('{'): raw_data.rfind('}')+1]
            data_dict = json.loads(raw_data)
            user = data_dict["entry_data"]["ProfilePage"][0]["graphql"]["user"]
            profile = user["biography"]
            attributes["email"] = get_email(profile)
            attributes["phone"] = get_phone(profile)
        return (attributes, data_dict)
