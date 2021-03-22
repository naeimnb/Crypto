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


bit_live=bit_live[1:].split(' ')
bit_live=bit_live[0]
print('bit_live: ',bit_live)

bit_24h_Volume=bit_24h_Volume[1:].split(' ')
bit_24h_Volume=bit_24h_Volume[0]
print('bit_24h_volume: ',bit_24h_Volume)

bit_Circulating_Supply=bit_Circulating_Supply.split(' ')
bit_Circulating_Supply=bit_Circulating_Supply[0]
print('bit_Circulating_Supply: ',bit_Circulating_Supply)

bit_Market_Cap=bit_Market_Cap[1:].split(' ')
bit_Market_Cap=bit_Market_Cap[0]
print('bit_Market_Cap: ',bit_Market_Cap)

bit_Max_Supply=bit_Max_Supply.split(' ')
bit_Max_Supply=bit_Max_Supply[0]
print('bit_Max_Supply: ',bit_Max_Supply)

bit_Yesterday_High_Low=bit_Yesterday_High_Low[1:].split(' ')
bit_Yesterday_High=bit_Yesterday_High_Low[0]
print('bit_Yesterday_High: ',bit_Yesterday_High)

bit_Yesterday_Low=bit_Yesterday_High_Low[3]
bit_Yesterday_Low=bit_Yesterday_Low[1:]
print('bit_YesterdayLow: ',bit_Yesterday_Low)

bit_Yesterday_Market_Cap=bit_Yesterday_Market_Cap[1:].split(' ')
bit_Yesterday_Market_Cap=bit_Yesterday_Market_Cap[0]
print('bit_Yesterday_Market_Cap: ',bit_Yesterday_Market_Cap)

bit_Yesterday_Open_Close=bit_Yesterday_Open_Close[1:].split(' ')
bit_Yesterday_Open=bit_Yesterday_Open_Close[0]
print('bit_Yesterday_Open: ',bit_Yesterday_Open)

bit_Yesterday_Close=bit_Yesterday_Open_Close[3]
bit_Yesterday_Close=bit_Yesterday_Close[1:]
print('bit_Yesterday_Close: ',bit_Yesterday_Close)

bit_Yesterday_Volume=bit_Yesterday_Volume[1:].split(' ')
bit_Yesterday_Volume=bit_Yesterday_Volume[0]
print('bit_Yesterday_Volume: ',bit_Yesterday_Volume)

