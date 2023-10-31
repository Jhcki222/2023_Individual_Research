from selenium.webdriver import ChromeOptions, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# YouTube 동영상 페이지로 이동
driver.get("https://www.youtube.com/watch?v=kGR4CGGTse8")

# 스크롤을 자동으로 내리는 동안 대기하기 위한 sleep 시간
SCROLL_PAUSE_TIME = 2

# 댓글 영역으로 스크롤하기
driver.execute_script("window.scrollTo(0, window.scrollY + 500);")
time.sleep(SCROLL_PAUSE_TIME)

# 스크롤 다운 반복
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    # 댓글 영역까지 스크롤
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    
    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 크롬의 개발자도구 -> ctrl+shift+c -> 댓글의 속성 파악
comments = driver.find_elements(By.CSS_SELECTOR,"yt-formatted-string#content-text")

# 댓글 텍스트 추출
comment_texts = [comment.text for comment in comments]

df = pd.DataFrame({'Comments': comment_texts})
df.to_excel("test2.xlsx")

input("Press Enter to close the browser...")
driver.quit()
