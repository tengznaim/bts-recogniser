import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

search_queries = ["jungkook bts portrait",
                  "v bts portrait", "jimin bts portrait"]
training_data_path = os.path.join(os.getcwd(), "training")

for query in search_queries:
    folder_path = os.path.join(training_data_path, query[:query.index(" ")])

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    driver.get("https://images.google.com/")

    search_box = driver.find_element_by_xpath(
        '//*[@id="sbtc"]/div/div[2]/input')
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)

    for i in range(1, 10):
        try:
            save_name = f'{query[:query.index(" ")]}({i}).png'
            save_path = os.path.join(folder_path, save_name)

            thumbnail = driver.find_element_by_xpath(
                f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')
            thumbnail.click()

            picture = driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img')
            time.sleep(1)
            url = picture.get_attribute("src")
            urllib.request.urlretrieve(url, save_path)

        except:
            pass

driver.quit()
