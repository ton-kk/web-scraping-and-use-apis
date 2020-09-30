import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                         "537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
maxView = 5
searchKey = "Google.com"


searchResult = requests.get("https://www.google.com/search",
                            params={"q": searchKey, "num": maxView}, headers=headers)
bs = BeautifulSoup(searchResult.text, 'html.parser')
ret_link = bs.select('.r > a')

for i in range(maxView):
    print(ret_link[i].get_text())
    url_link = ret_link[i].get('href').replace('/url?q=', '')
    print(url_link)
