from bs4 import BeautifulSoup
import requests

url = 'https://coin360.com/coin/bitcoin-btc'
res = requests.get(url)
res = res.text
soup = BeautifulSoup(res, 'html.parser')

bit_live = soup.find('td', attrs={'class':'ExtraInfoBlock__InfoBlockValue'})
bit_live= bit_live.text
print(bit_live)
