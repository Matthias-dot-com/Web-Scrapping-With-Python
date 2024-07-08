from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# Other methods

# dictionary = {}

# times = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
# links = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')

# i = 0
# for time,event  in zip(times,links):
#     dictionary[i] = {"time" :time.text,"event" :event.text }
#     i+=1

times = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget time")
links = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget li a")

dictionary = {}


for i in range(len(times)):
    dictionary[i] = {
        "time":times[i].text,
        "event" : links[i].text
    }

print(dictionary)
driver.close()