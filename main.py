import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
import socket

randomnames="peter paul james jhon harry anna mary clive sharon david mateo"
randomnames=randomnames.split()
randomlastnames="dickerson cortez styles smith washington thompson oconnel odonavan kardi"
randomlastnames=randomlastnames.split()
randomlettersandnumbers="tr12145 tryu6579 qasx6743 poi432 wqas568 fvcnm674 erwqasc rr144"
randomlettersandnumbers=randomlettersandnumbers.split()
mailpaswrd=random.choice(randomlettersandnumbers)+random.choice(randomlettersandnumbers)

usermail=random.choice(randomnames)+random.choice(randomlastnames)+random.choice(randomlettersandnumbers)
driver=webdriver.Chrome()
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&dsh=S285974031%3A1649874346464508&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")
while True:
    try:
        driver.find_element(By.XPATH,'//*[@id="firstName"]').send_keys(random.choice(randomnames))
        driver.find_element(By.XPATH,'//*[@id="lastName"]').send_keys(random.choice(randomlastnames))
        driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(usermail)
        driver.find_element(By.XPATH,'//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys(mailpaswrd)
        driver.find_element(By.XPATH,'//*[@id="confirm-passwd"]/div[1]/div/div[1]/input').send_keys(mailpaswrd)
        break
    except:
        pass
driver.find_element(By.XPATH,'//*[@id="accountDetailsNext"]/div/button').click()
while True:
    try:
        driver.find_element(By.XPATH,'//*[@id="phoneNumberId"]').send_keys("832085932")
        break
    except:
        pass
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
ADDR=(ip,5050)
server.bind((ADDR))
def serverbind():
    while True:
        conn,addr=server.accept()
        codemsg=conn.recv(64)
        codemsg.decode('utf-8')
driver.find_element(By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
time.sleep(4)
try:
    driver.find_element(By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[2]/div').text
    googlefaild=True
    driver.get("https://login.yahoo.com/account/create?.src=ym&pspid=1197806870&activity=header-signup&.lang=en-IE&.intl=ie&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3F.intl%3Die%26.lang%3Den-IE%26pspid%3D2142167817%26activity%3Dybar-mail&authMechanism=primary&specId=yidReg")
    driver.find_element(By.XPATH,'//*[@id="usernamereg-firstName"]').send_keys(random.choice(randomnames))
    driver.find_element(By.XPATH,'//*[@id="usernamereg-lastName"]').send_keys(random.choice(randomlastnames))
    driver.find_element(By.XPATH,'//*[@id="usernamereg-yid"]').send_keys(usermail)
    driver.find_element(By.XPATH,'//*[@id="usernamereg-phone"]').send_keys("832085932")
    driver.find_element(By.XPATH,'//*[@id="usernamereg-month"]').click()
    while True:
        try:
            driver.find_element(By.XPATH,'')
            break
        except:
            pass
except:
    pass
vercode=input("VERIFICATION CODE: ")
while True:
    try:
        driver.find_element(By.XPATH,'//*[@id="code"]').send_keys(vercode)
        break
    except:
        pass
driver.find_element(By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button')
print('dont ') 
