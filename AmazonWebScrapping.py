import requests
from bs4 import BeautifulSoup
import smtplib as smtp


url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
req = requests.get(url,headers={'Accept-Language' :'en-US,en;q=0.9' ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'})

if req.status_code == 200:
    soup = BeautifulSoup(req.content, 'html.parser')

    product_title = soup.find('span', class_="a-price-whole").get_text().strip()
    product_cents = soup.find("span", class_= "a-price-fraction").get_text().strip()

    print(f"Product Title: {product_title}{product_cents}$")

else:
    print(f"Failed to retrieve data from {url}. Status code: {req.status_code}")

sender_email='SENDER EMAIL'
password='SENDER PASSWORD'
recipient_email='RECEIVER EMAIL'


with smtp.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=sender_email,password=password)
    connection.sendmail(from_addr=sender_email,to_addrs=recipient_email,subject="hello",msg=f"The price of the cooker you are looking for is  {product_title}{product_cents}")
    print('successfully sent')