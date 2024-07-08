from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_option)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

numberOfArticles = driver.find_element(by=By.XPATH, value = '//*[@id="articlecount"]/a[1]').text
print(numberOfArticles)


driver.close()