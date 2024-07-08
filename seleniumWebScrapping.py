from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.ae/dp/B0BS1PH5N3")

price_cash = driver.find_element(By.CLASS_NAME,"a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME,"a-price-fraction").text

search_bar = driver.find_element(By.NAME,"field-keywords")
button = driver.find_element(By.CSS_SELECTOR,"input[type=submit]")
search_icon = driver.find_element(By.XPATH,value='//*[@id="acrCustomerReviewText"]').text
print(search_icon)
# price = f'{price_cash}.{price_cents}'
# print(price)
# print(search_bar.get_attribute("class"))
# print(button.size)
driver.close()
# driver.quit is also possible it will close the whole browser
