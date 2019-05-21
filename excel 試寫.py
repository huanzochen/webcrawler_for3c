import xlwt 
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet('hello') #在其中建立一個名為hello的sheet 
sheet1.write(0,0,'cloudox') #往sheet裡第一行第一列寫一個資料 
sheet1.write(1,0,'ox') #往sheet裡第二行第一列寫一個資料 
book.save("test.xls") #建立儲存檔案#
#主函數
