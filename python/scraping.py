from bs4 import BeautifulSoup 
import urllib.request
from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from PIL import Image # pip3 install pillow
from datetime import datetime
now = datetime.now()

search=""
#userid = ""
#userpw = "" 여기에 MS 계정 정보 입력하거나 
def init_driver():
    
    userid = input("로그인 - Mincrosoft 아이디를 입력하세요.")
    userpw = input("로그인 - Mincrosoft 비밀번호를 입력하세요.")
    path = r"C:\Users\qkrtj\Desktop\23-record\pieceDream\python\selenium\chromedriver.exe"
    driver = webdriver.Chrome(path)
    
    driver.get('https://www.bing.com/fd/auth/signin?action=interactive&provider=windows_live_id&return_url=https%3a%2f%2fwww.bing.com%2fimages%2fcreate%3fsude%3d1&cobrandid=03f1ec5e-1843-43e5-a2f6-e60ab27f6b91&noaadredir=1&FORM=GENUS1')
    driver.implicitly_wait(3)

    driver.find_element(By.ID,"i0116").send_keys(userid)

    driver.find_element(By.ID, "idSIButton9").click()

    
    driver.find_element(By.ID,"i0118").send_keys(userpw)
    time.sleep(2)
    
    driver.find_element(By.ID, "idSIButton9").click()
    driver.find_element(By.ID, "idBtn_Back").click()
    
    return driver

def search_(driver):

    driver.find_element(By.ID,"sb_form_q").send_keys(search)
    time.sleep(2)

    driver.find_element(By.ID, "create_btn_c").click()
    print("1분간 기다려 주세요...")
    time.sleep(30)
    print("sleep 끝")


if  __name__  ==  "__main__" :
    search = input("검색어를 입력하세요")
    driver = init_driver()
    search_(driver)

    #상위 클래스(전체박스)
    v = driver.current_url
    print(v)
    now = now.strftime("%Y%m%d_%H.%M")
    path = "./img/"
    os.chdir(path)
    divbox = driver.find_element(By.CLASS_NAME, "mimg").get_attribute("src")
    urllib.request.urlretrieve(divbox, now + "img.jpg")
    print('다운로드 완료')
    img = Image.open(now+ "img.jpg")
    img.show()

