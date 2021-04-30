import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from skimage import io
import imutils
import cv2 as cv
import os
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

search_queries = ["jungkook bts portrait",
                  "v bts portrait", "jimin bts portrait", "jin bts portrait", "suga bts portrait", "j-hope bts portrait", "rm bts portrait"]
training_data_path = os.path.join(os.getcwd(), "training")
haar_cascade = cv.CascadeClassifier(os.path.join(
    os.getcwd(), "haarcascade_frontalface_default.xml"))

for query in search_queries:
    folder_path = os.path.join(training_data_path, query[:query.index(" ")])

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    driver.get("https://images.google.com/")

    search_box = driver.find_element_by_xpath(
        '//*[@id="sbtc"]/div/div[2]/input')
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)

    i = 0
    img_count = 1

    while img_count != 10:
        i += 1
        print(i)
        try:
            thumbnail = driver.find_element_by_xpath(
                f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')
            thumbnail.click()

            picture = driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img')
            time.sleep(1)
            url = picture.get_attribute("src")

            original = io.imread(url)
            detected = cv.cvtColor(imutils.resize(
                original, height=min(original.shape[0], 600)), cv.COLOR_RGB2BGR)
            gray = cv.cvtColor(detected, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=3)

            if len(faces_rect) == 1:

                for x, y, w, h in faces_rect:
                    cv.rectangle(detected, (x, y), (x+w, y+h), (0, 255, 0))

                cv.imshow("Image", detected)
                cv.waitKey(0)

                user_validation = input("Save this image? y/n:")

                if user_validation == "y":
                    save_name = f'{query[:query.index(" ")]}({img_count}).png'
                    save_path = os.path.join(folder_path, save_name)
                    io.imsave(save_path, original)
                    img_count += 1

        except:
            pass

driver.quit()
