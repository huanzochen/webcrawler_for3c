import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

res = requests.get('https://www.fun123.com.tw/')
soup = BeautifulSoup(res.text,'html.parser')
#htmllist = res.text.splitlines()
#itname = soup.select('.deal-name')
#itname = soup.select('.deals')
#itdealinfo = soup.find_all('div',{'class':'deal-info'})
itprice = soup.find_all('div',{'class':'price'})
#itpriceoffer = itprice.find_all('i',{'':''})

#itname2 = itname.select('.deal_name')
item3href = []
for item in soup.select('.deals'):
    item2=item.select('.deal_name')
    
for i in range(0,len(item2)):
    item3href.append(len(item2))
    item3href[i]=item2[i].get('href')
    #print(item3href)
"""
for k in range(0,len(item3href)):   
    #print(item3href[k])
"""
item3offer = []
item3origin = []

for n in range(0,10,1):
    #print(n)
    res2 = requests.get('https://www.fun123.com.tw'+item3href[n])
    soup2 = BeautifulSoup(res2.text,'html.parser')
    offerprice = soup2.select('.big_price')
    originprice = soup2.select('del')
    item3offer.append(1)
    item3origin.append(1)
    #(originprice[1].text)為原價 2480
    #(offerprice[0].text) 特價 1480
    item3offer[n] = (offerprice[0].text)
    item3origin[n] = (originprice[1].text)

for i in range(0,len(item2)):
    print(item2[i].text)


    
