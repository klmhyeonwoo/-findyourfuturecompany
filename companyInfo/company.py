from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from io import BytesIO
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import json
import os

chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')               # headless
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920x1080')

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service = service, options = chrome_options)
driver.implicitly_wait(3)
driver.get('https://www.jobkorea.co.kr/starter/calendar')

parsing_data = {}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

def processing(data):
    try:
        data.click()
        sleep(1)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        companyLink = soup.select('div.co > div.coTit > a.coLink')
        companyState = soup.select('div.co > div.coTit > a.coLink > span > strong:nth-child(1)')
        companyName = soup.select('div.co > div.coTit > a.coLink > span')
        companyContent = soup.select('div.info > div.tit > a.link > span')
        companyPosition = soup.select('div.sDesc > strong')
        companyPlan = soup.select('div.side > span.day')

        for link, name, state, content, position, plan in zip(companyLink, companyName, companyState, companyContent, companyPosition, companyPlan):
            state = state.get_text().strip()
            link = link.get('href')
            name = name.get_text().strip()[2:]
            content = content.get_text().strip()
            position = position.get_text().strip()
            plan = plan.get_text().strip()

            #if state == "시작" or state == "예상":
            print(state, name, content, position, plan, link)
            parsing_data[name] = {
                "state" : state,
                "content" : content,
                "position" : position,
                "plan" : plan,
                "link" : link,
            }

        driver.find_element(By.CSS_SELECTOR,'button.closeCalLy').click()

    except Exception as e:
        print(e)
        return None

infolst1 = driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(1) > td.sunday > div > div > div > span.moreNum')
infolst1 = infolst1 + driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(1) > td > div > div > div > span.moreNum')
infolst1 = infolst1 + driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(1) > td.saturday > div > div > div > span.moreNum')
infolst2 = driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(2) > td.sunday > div > div > div > span.moreNum')
infolst2 = infolst2 + driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(2) > td > div > div > div > span.moreNum')
infolst2 = infolst2 + driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(2) > td.saturday > div > div > div > span.moreNum')
infolst3 = driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(3) > td.sunday > div > div > div > span.moreNum')
infolst3 = infolst3 + driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(3) > td > div > div > div > span.moreNum')
infolst3 = infolst3 + driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(3) > td.saturday > div > div > div > span.moreNum')
infolst4 = driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(4) > td.sunday > div > div > div > span.moreNum')
infolst4 = infolst4 + driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(4) > td > div > div > div > span.moreNum')
infolst4 = infolst4 + driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(4) > td.saturday > div > div > div > span.moreNum')
infolst5 = driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(5) > td.sunday > div > div > div > span.moreNum')
infolst5 = infolst5 + driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(5) > td > div > div > div > span.moreNum')
infolst5 = infolst5 + driver.find_elements(By.CSS_SELECTOR,'#container > div.stContainer > div.calContent > div.starNowMonth > table > tbody > tr:nth-child(5) > td.saturday > div > div > div > span.moreNum')

infolst = infolst1 + infolst2 + infolst3 + infolst4 + infolst5

for data in infolst:
    if (processing(data) != None):
        print(processing(data))
driver.quit()


with open(os.path.join(BASE_DIR, 'news.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(parsing_data, json_file, ensure_ascii = False, indent='\t')

print("완료!")
