import requests
from bs4 import BeautifulSoup
res2 = requests.get('https://www.fun123.com.tw/site/sku/2041431/%E8%81%B2%E5%AF%B616%E5%90%8B%E6%BA%AB%E6%8E%A7%E9%81%99%E6%8E%A7DC%E9%9B%BB%E6%89%87?cid=115654#?ref=d_index_all_20') #前往其他商品連結
soup2 = BeautifulSoup(res2.text,'html.parser')
origin = soup2.select('.left selectorgadget_selected')
origin2 = soup2.select('.buy_area_discount')
origin3 = soup2.select('.left')
origin4 = origin3[0].select('.left')
origin5 = soup2.find('div',{"class":"left"})
"""
print(len(origin))
print(len(origin2))
print(origin2[0])
print(len(origin3))
print(origin3)
"""
print(len(origin5))
print(origin5.text)
