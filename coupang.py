import requests
from bs4 import BeautifulSoup

class Product:
    def __init__(self, url):
        self.url = url
        self.title = None
        self.origin_price = None
        self.total_price = None
        self.discount = None
        self.shipping_cost = None
        self.rating = None
        self.rating_cnt = None
        self.delivery_date = None
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
    
    def get_data(self):
        r = requests.get(self.url, headers=self.headers)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        
        #get title
        try:
            self.title = soup.find("h2", {"class": "prod-buy-header__title"}).text.strip()
        except:
            self.title = "제목 없음"
        
        #get origin_price
        try:
            self.origin_price = int(soup.find("span", {"class": "origin-price"}).text.replace(',', '').replace('원', ''))
        except:
            self.origin_price = int(soup.find("span",{"class":"total-price"}).find("strong").text.replace(',', '').replace('원', ''))
        
        #total price
        try:
            self.total_price = int(soup.find("span",{"class":"total-price"}).find("strong").text.replace(',', '').replace('원', ''))
        except:
            pass
        
        #discount
        try:
            self.discount = float(soup.find("span", {"class": "discount-rate"}).text.strip("%"))
        except:
            pass
        
        #shipping cost
        try:
            self.shipping_cost = soup.find("em", {"class": "prod-txt-bold"}).text
        except:
            pass
        
        #rating
        try:
            self.rating = float(soup.find("span", {"class": "rating-star-num"})["style"].strip("width:").strip("%;"))
        except:
            pass
        
        #rating count
        try:
            self.rating_cnt = int(soup.find("span", {"class": "count"}).text.strip('개 상품평'))
        except:
            pass
        
        #delivery date
        try:
            self.delivery_date = soup.find("em", {"class": "prod-txt-onyx prod-txt-green-2"}).text
        except:
            self.delivery_date = soup.find("em", {"class": "prod-txt-onyx prod-txt-font-14"}).text

