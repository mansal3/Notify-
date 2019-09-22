#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:23:56 2019

@author: manpreetsaluja
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:04:23 2019

@author: manpreetsaluja
"""

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

url="https://www.amazon.in/255-Bluetooth-Wireless-Earphone-Immersive/dp/B07C2VJFDW?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=_k_Cj0KCQjwlJfsBRDUARIsAIDHsWrkS7IqHS5YJZGxyDZa61rSkkK_7wXhbX1RcIvLyeFxUs72gflgGkUaAupbEALw_wcB_k_&gclid=Cj0KCQjwlJfsBRDUARIsAIDHsWrkS7IqHS5YJZGxyDZa61rSkkK_7wXhbX1RcIvLyeFxUs72gflgGkUaAupbEALw_wcB"

browser_agent={"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

productpage=requests.get(url,headers=browser_agent)

soup=BeautifulSoup(productpage.content,'html.parser')

print(soup.prettify())

pagetitle=soup.find(id="productTitle").get_text()

product_price=soup.find(id="priceblock_ourprice").get_text()[2:7]
product_price=product_price.replace(',','')
product_price=float(product_price)

if(product_price<1500):
    send_email()
    
    
    def send_email():

    msg = MIMEMultipart()    
    message = "price is low now !!!"+pagetitle
    password = "yourpassword"
    msg['From'] = "sendemail"
    msg['To'] = "receviver email"
    msg['Subject'] = "Hurry!!!!! grab the offer"
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')    
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())    
    server.quit()
    print ("successfully sent email to %s:" % (msg['To']))
         
 

     
    
    
