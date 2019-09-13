from bs4 import BeautifulSoup
import requests

# url = requests.get("https://sdk.semarangkota.go.id/komunitas/datapenggunaanruangan.php?data=lainnya")

class ScrapperSdk:
    def __init__(self, url):
        self.url = requests.get(url)
        self.content = []

    def get(self):
        soup = BeautifulSoup(self.url.text, 'html.parser')
        tr = soup.find_all('tr', class_ = 'gradeX')

        content = []
        for td in tr:
            content.append({
                "date": td.findChildren('td')[1].text,
                "time": td.findChildren('td')[2].text,
                "room": td.findChildren('td')[3].text,
                "community": td.findChildren('td')[4].text.strip(),
                "contact": td.findChildren('td')[5].text,
                "desc": td.findChildren('td')[6].text
            })        
        self.content = content
        return self.content 