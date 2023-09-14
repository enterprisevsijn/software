import re
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pyperclip import paste
from selenium.webdriver import ChromeOptions
import requests

options = ChromeOptions()
options.add_argument('headless')
web = Chrome(options=options)
url = "https://www.luogu.com.cn/problem/P"
cookie = {
    'login_referer': 'https%3A%2F%2Fwww.luogu.com.cn%2Fproblem%2FP1000',
    '_uid': '111884',
    '__client_id': '4f1bbbf98da6e49a6c98727320089c851c18d53c',
    'C3VK': 'aa6e71',
}
index = 1000
while index < 9640:
    search_url = url + str(index)
    web.get(search_url)
    web.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/main/div/section[2]/section/div/div[1]/a[1]').click()
    title = web.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[1]/div[2]/h1/span').text

    title = re.sub("\[.*?\] ", '', title)
    title = title.replace(' ', '-', 1).replace('/', '-')
    title = 'temp/' + title + '.md'
    f = open(title, mode='w', encoding='utf-8')
    f.write(paste())
    f.close()
    index += 1

while True:
    continue
