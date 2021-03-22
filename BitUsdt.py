from bs4 import BeautifulSoup
import requests

url = 'https://coin360.com/coin/bitcoin-btc'
res = requests.get(url)
res = res.text
soup = BeautifulSoup(res, 'html.parser')

myBitSoup = soup.find_all('td', attrs={'class': 'ExtraInfoBlock__InfoBlockValue'})
select=0
for item in myBitSoup:
    item=item.text
    if select==0:
        bit_live=item
    if select==2:
        bit_Market_Cap=item
    if select==3:
        bit_24h_Volume=item
    if select==4:
        bit_Circulating_Supply=item
    if select==5:
        bit_Max_Supply=item
    if select==6:
        bit_Yesterday_Market_Cap=item
    if select==7:
        bit_Yesterday_Open_Close=item;
    if select==8:
        bit_Yesterday_High_Low=item
    if select==10:
        bit_Yesterday_Volume=item
    select+=1


print('bit_live: ',bit_live)
print('bit_24h_volume: ',bit_24h_Volume)
print('bit_Circulating_Supply: ',bit_Circulating_Supply)
print('bit_Market_Cap: ',bit_Market_Cap)
print('bit_Max_Supply: ',bit_Max_Supply)
print('bit_Yesterday_High_Low: ',bit_Yesterday_High_Low)
print('bit_Yesterday_Market_Cap: ',bit_Yesterday_Market_Cap)
print('bit_Yesterday_Open_Close: ',bit_Yesterday_Open_Close)
print('bit_Yesterday_Volume: ',bit_Yesterday_Volume)

