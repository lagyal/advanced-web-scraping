from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

s = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=s)

driver.get('https://www.smartprix.com/mobiles/exclude_out_of_stock-exclude_upcoming-stock')
time.sleep(2)

# driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/aside/div/div[5]/div[2]/label[1]/input').click()
# time.sleep(2)
#
# driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/aside/div/div[5]/div[2]/label[2]/input').click()
# time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')
print(old_height)

count = 0
while True:

    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(5)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(count)
    count += 1
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source

with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)



