import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
res = requests.get('https://www.fun123.com.tw/',headers=headers)
htmllist = res.text.splitlines()
soup = BeautifulSoup(res.text,'html.parser')
#itname = soup.select('.deal-name')
itname = soup.find_all('h3',{'class':'deal-name'})
"""for n in range(0,len(itname)-1):
    print(itname[n])
"""

itdealinfo = soup.find_all('div',{'class':'deal-info'})
itprice = soup.find_all('div',{'class':'price'})
#itpriceoffer = itprice.find_all('i',{'':''})

"""
for k in range(0,len(itprice)):
    print(itname[k].text,"\n",itprice[k].text)
"""
"""
for i in range(0,(len(itprice)-1)):
    print("第{}個字串的長度為:".format(i),len(itprice[i].text))
    print("TTT"+itprice[i].text+"TTT")
"""
"""
name="黃子銓"
name_unicode=u"黃子銓"
print(len(name))
print(len(name_unicode))
"""
namewithnum="特價 $650起  原價$2990"
price=namewithnum.split(' ')
offer=price[1].split('$')
origin=price[-1].split('原價$')
print(offer[-1])
print(origin[-1])    
#for i in price:
#    print(i)