import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
res = requests.get('https://www.fun123.com.tw/', headers=headers)
htmllist = res.text.splitlines()
soup = BeautifulSoup(res.text,'html.parser')
itgroup = soup.select('.deals')
#itname = itgroup.find_all('h3',{'class':'deal-name'})
itprice = itgroup[0].find('div',{'class':'price'})
print(itname)



