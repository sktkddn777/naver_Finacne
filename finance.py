from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1"
driver.get(url)

for i in range(1, 32):
    url = f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={i}"

    for j in range(2, 79): #2~78 : tr개수
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        try:
            check = soup.select_one(f"#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child({j}) > td:nth-child(2)")
            if not check or check.get_text() == 'N/A':
                pass
            else:
                stock_code = soup.select_one(f'div.box_type_l > table.type_2 > tbody > tr:nth-child({j}) > td:nth-child(2) > a')
                stock_name = soup.select_one(f'div.box_type_l > table.type_2 > tbody > tr:nth-child({j}) > td:nth-child(2) > a').get_text()
                stock_price = soup.select_one(f'div.box_type_l > table.type_2 > tbody > tr:nth-child({j}) > td:nth-child(3)').get_text()
                stock_trade = soup.select_one(f'div.box_type_l > table.type_2 > tbody > tr:nth-child({j}) > td:nth-child(10)').get_text()
                stock_PER = soup.select_one(f'div.box_type_l > table.type_2 > tbody > tr:nth-child({j}) > td:nth-child(11)').get_text()
                stock_ROE = soup.select_one(f'div.box_type_l > table.type_2 > tbody > tr:nth-child({j}) > td:nth-child(12)').get_text()
                driver.implicitly_wait(3)
                print(stock_name + stock_price + stock_PER)
                # url2 = 'https://finance.naver.com/'+stock_code['href']
                # driver.get(url2)
                # html = driver.page_source
                # soup = BeautifulSoup(html, 'html.parser')
        except:
            pass





# depth_1_tbody = driver.find_element_by_xpath("//*[@id='contentarea']/div[@class='box_type_l']/table/tbody") #tbody로 xpath생성
# depth_2_tr = depth_1_tbody.find_elements_by_tag_name("tr") #xpath를 가지고 tr을 탐색(tr이 여러개이므로) tr -> 순위당 하나씩
# print(depth_2_tr[0])


# elem = driver.find_elements_by_css_selector("title")/div[0]/div[1]/div[2]/table/tbody
# print(elem)

# SCROLL_PAUSE_SEC = 1
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_SEC)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         try:
#             driver.find_element_by_css_selector(".mye4qd").click()
#         except:
#             break
#     last_height = new_height
    
# driver.close()