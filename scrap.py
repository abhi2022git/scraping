from lxml import etree
import requests
from bs4 import BeautifulSoup 
import time
import csv
import import_smtplib 
urls = ["https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch","https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch","https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch"]

headers = {'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

csv_file = open("stockdata.csv","w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title','Stock value','Privious Close','Open','Bid','Ask','Day\'s Range','52 Week Range','Volume','Avg. Volume'])

for url in urls:
    List = []

    html_page = requests.get(url,headers=headers)

    soup = BeautifulSoup(html_page.content,'lxml')


    header_info = soup.find_all('div',id='quote-header-info')[0]
    title_info = header_info.find('h1').get_text()
    stock_info = header_info.find('div',class_='D(ib) Va(m) Maw(65%) Ov(h)').find('fin-streamer').get_text()

    List.append(title_info)
    List.append(stock_info)




    table_info = soup.find_all('div',class_='D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')[0].find_all('tr')
    for i in range(0,8):
        heading = table_info[i].find_all('td')[0].get_text()
        value = table_info[i].find_all('td')[1].get_text()

        List.append(value)

        

    csv_writer.writerow(List)
   
    time.sleep(5)
csv_file.close()

import_smtplib.send(filename='stockdata.csv')



