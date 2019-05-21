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
"""
for item in soup.select('.deals'):
    item2=item.select('.deal_name')
for i in range(0,len(item2)):
    print(item2[i].text)
"""
#以上可取得物品名稱 item2為lazyitem


#print("共跑了{}次".format(i))

"""
for i in range(0,len(itname2)):
    print(itname2[i])
print("共跑了{}次".format(i))
"""


