import urllib
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#driver = webdriver.Chrome()
#driver.get("https://www.yahoo.co.jp")
#login_btn = driver.find_element_by_xpath('//*[@id="Login"]/div/p[1]/a')
#login_btn.click()
#time.sleep(1)
#login_id = driver.find_element_by_name("login")
#login_id.send_keys("ログインIDを入力")
#next_btn = driver.find_element_by_name("btnNext")
#next_btn.click()
#time.sleep(1)
#password = driver.find_element_by_name("passwd")
#password.send_keys("パスワードを入力")
#time.sleep(1)
#login_btn = driver.find_element_by_name("btnSubmit")
#login_btn.click()
#url = requests.get('https://cas.kumamoto-u.ac.jp/cas/login?service=https%3A%2F%2Fmd.kumamoto-u.ac.jp%2Flogin%2Findex.php')
#url.raise_for_status()
#soup = BeautifulSoup(url.text,'html.parser')
#elem = soup.select('')
#print(elem)


Token = 'Ev98TioEKI2oWPTYGWW9i0fNTJF5Zu9ETUG6LlGHh42'
api_url = 'https://notify-api.line.me/api/notify'
send_contents_1 = '虎太郎さん \n日付を超えたらゼミの資料を印刷してください\n'
send_contents_2 ='結婚式の日のホテルの予約をしてください。'
Token_dic = {'Authorization': 'Bearer' + ' ' + Token}
send_dic_1 = {'message':send_contents_1}
send_dic_2 = {'message':send_contents_2}
cut =[send_dic_1,send_dic_2]
for i in range(2):
    requests.post(api_url,headers = Token_dic,data = cut[i])
