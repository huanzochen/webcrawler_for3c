import requests
from bs4 import BeautifulSoup
from tempfile import TemporaryFile
from xlwt import Workbook
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
s = requests.Session()
res = s.get('https://www.fun123.com.tw/')
soup = BeautifulSoup(res.text,'html.parser')
#以下為爬首頁重點商品,共九樣
itname = soup.find_all('h3',{'class':'deal-name'})
itprice = soup.find_all('div',{'class':'price'})
#將主力商品的價格轉為純數字
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
#for q in range(0,len(itname)):
    #print(itofferprice[q])
    #print(itoriginprice[q])

#為其他商品,共804樣  (len(item3href))
#先從首頁得到lazy商品(網站重點商品以外的其他商品的名稱和他的連結)

item3href = []
for item in soup.select('.deals'):
    item2=item.select('.deal_name')   
for i in range(0,len(item2)):
    item3href.append(len(item2))
    item3href[i]=item2[i].get('href')

#將連結存進item3href,特價存入item3offer,原價存入item3origin
item3offer = []
item3origin = []
item3offerfull = []
item3originfull = []
#總共要爬len(item3href)共804樣其他商品,預計會載入804個網頁取得其中的值

print("開始蒐集其他商品資訊...正在爬第...個網頁,共{}個".format(len(item3href)))
for n in range(0,len(item3href),1):
    print("{},".format(n+1),end="")
    res2 = requests.get('https://www.fun123.com.tw'+item3href[n])#前往其他商品連結
    soup2 = BeautifulSoup(res2.text,'html.parser')
    offerprice = soup2.select('.big_price')#特價
    originprice = soup2.select('del')#原價
    offerpricefull = soup2.select('.buy_area_price_tag')#特價包含起
    originpricefull = soup2.find('div',{"class":"left"})#select不好找改用find
    
    item3offer.append(1)
    item3origin.append(1)
    item3offerfull.append(1)
    item3originfull.append(1)
    #(originprice[1].text)為原價 "2480" 此項目隨著爬到的商品改變
    #(offerprice[0].text) 特價 "1480"  此項目隨著爬到的商品改變
    
    item3offer[n] = (offerprice[0].text)
    item3origin[n] = (originprice[1].text)
    item3offerfull[n] = (offerpricefull[0].text)
    item3originfull[n] = (originpricefull.text)
#print(item3offerfull[0])
#print(item3originfull[0])
print("\n\n主力商品:") 
for k in range(0,len(itprice)):   
    print(itname[k].text,itprice[k].text)
print("\n其他商品:")
for i in range(0,len(item3href)):
    print(item2[i].text,item3offerfull[i],item3originfull[i])

book = Workbook()
sheet1 = book.add_sheet('商品報價單')
sheet1.write(0,0,'商品名稱')
sheet1.write(0,1,'原價')
sheet1.write(0, 2, '特價')
row1 = sheet1.row(1)
row1.write(0,'主力商品:')
row1 = sheet1.row(12)
row1.write(0,'其他商品:')
#sheet1.write(12, 0, '其他商品:')

for mainitem in range(0,len(itname)):
    row1 = sheet1.row(mainitem+2)
    row1.write(0,itname[mainitem].text)
    row1.write(1,itofferprice[mainitem])
    row1.write(2,itoriginprice[mainitem])
for other in range(0,len(item3href)):
    row2 = sheet1.row(other+13)
    row2.write(0,item2[other].text)
    row2.write(1,item3offer[other])
    row2.write(2,item3origin[other])

sheet1.col(0).width = 10000
book.save('3c市集首頁商品目錄.xls')
book.save(TemporaryFile())