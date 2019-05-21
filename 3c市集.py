import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
s = requests.Session()
res = s.get('https://www.fun123.com.tw/')
soup = BeautifulSoup(res.text,'html.parser')
#htmllist = res.text.splitlines()
#itname = soup.select('.deal-name')
itname = soup.find_all('h3',{'class':'deal-name'})
#itdealinfo = soup.find_all('div',{'class':'deal-info'})
itprice = soup.find_all('div',{'class':'price'})
#itpriceoffer = itprice.find_all('i',{'':''})


itofferprice=[]
itoriginprice=[]
for g in range(0,len(itname)):
    price=(itprice[g].text).split(' ')
    offer=price[1].split('$')
    origin=price[-1].split('原價$')
    itofferprice.append(1)
    itoriginprice.append(1)
    itofferprice[g]=offer[-1]
    itoriginprice[g]=origin[-1]

for q in range(0,len(itname)):
    print(itofferprice[q])
    print(itoriginprice[q])





#for k in range(0,len(itprice)):
#   print(itname[k].text,itprice[k].text)






"""for i in range(0,len(itprice)):
    print(itprice[i].text)
"""




"""for price in itpriceoffer.text:
    print(price)
"""


"""for itprice in soup.select('.price'):
    print(itprice)
 """