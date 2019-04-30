#
#  Copyright (c) 2019 Yasuyuki Shigeno
#  All Rights Reserved.
#  written by Yasuyuki Shigeno
#
#  This program was developed by Yasuyuki Shigeno as a part of a
#  scraping system, titled "NikkeiScraping".
#  All the programs of the system is developed by
#  Yasuyuki Shigeno and all rights are reserved by Yasuyuki Shigeno.
#
#  Permission to use, copy, modify and distribute this software and
#  its documentation is hereby granted, provided that both the
#  copyright notice and this permission notice appear in all copies of
#  the software, derivative works or modified versions, and any
#  portions thereof, and that both notices appear in supporting
#  documentation.
#
#
#  @author Yasuyuki Shigeno
#  Created on 2019/04/14
#

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import chromedriver_binary
import time
import configparser
# from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from tkinter import messagebox
import pandas as pd

#グローバル変数
# config = None
# driver = None
# df = None
str_id = ""
str_pass = ""
el_login_id = ""
el_login_pass = ""
el_login_btn = ""
el_search_txtbox = ""

df = pd.DataFrame( columns=['記事タイトル','内容'] )
config = configparser.ConfigParser()
config.read('PyConfig.ini')
# ブラウザーを起動
options = Options()
options.binary_location = config.get('Browser', 'ChromeLocation')
options.add_argument('--headless')
options.add_argument('--window-size=1280,800')
driver = webdriver.Chrome(options=options, executable_path=config.get('Driver', 'ChromeDriverPath'))


# driver = webdriver.Chrome(config.get('Driver', 'ChromeDriverPath'))

#
# import chromedriver_binary


def setDefault():
    pass

def setElementId():
   el_login_id = 'LA7010Form01:LA7010Email'
   el_login_pass = 'LA7010Form01:LA7010Password'
   el_login_btn = 'LA7010Form01:submitBtn'
   el_search_txtbox = 'SEARCH_QUERY'


def login():
    driver.get(config.get('Nikkei', 'LoginUrl'))
    # ID/PASSを設定(ユーザ入力)
    print("Please input your Nikkei ID>")
    str_id = input()
    print("Please input your Nikkei Password")
    str_pass = input()
    elementID_UserId = driver.find_element_by_id(el_login_id)
    elementID_UserId.send_keys(str_id)
    elementID_Password = driver.find_element_by_id(el_login_pass)
    elementID_Password.send_keys(str_pass)
    time.sleep(1)
    # ログインボタンをクリック
    login_button = driver.find_element_by_id(el_login_btn)
    login_button.click()
    time.sleep(1)

# def enterKeyword():
    # keywordbox=driver.find_element_by_xpath("//*[@id='SEARCH_QUERY']")
    # keywordbox.send_keys("貿易")
    # driver.find_element_by_name(el_search_txtbox)
    # time.sleep(1)
    # keywordbox.send_keys(Keys.RETURN)
    #keywordbox.submit()
    # time.sleep(1)
    # driver.find_element_by_xpath("//*[@id='JSID_key_defaultsubmit']").submit()
    # driver.find_element_by_name(el_search_txtbox).send_keys(Keys.RETURN)
    # driver.execute_script("_nk.click(this,event,[['JSID_actFormSubmit']])")
    # driver.find_element_by_class_name("l-miH02_H02e_formSubmit").click()
    # driver.find_element_by_id("JSID_baseModalBackground")

def search():

    # サイト内で他の画面に遷移させたければ
    keyword = '貿易'
    try:
        driver.get(config.get('Nikkei', 'SearchUrl')+keyword)
    except:
        messagebox.showerror('URLエラー', '検索用URLが不正です。')
    # time.sleep(3)
    # enterKeyword()
    time.sleep(1)

def getDataSource(pages):
    count = 0

    while count <=pages:
        try:
            driver.find_element_by_xpath("/html/body/div[3]/main/div/div[5]/div/div[2]/button").click()
            count += 10
            time.sleep(2)
        except:
            break

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    headlines = soup.find_all("h3")
    subtexts = soup.find_all("a", class_="nui-card__excerpt")
    # subtexts = soup.find_all("div", class_="nui-card__sub-text")
    # subtexts2 = subtexts.find_all("mark", class_="search__highlight")
    # for headline in headlines:
    global df
    for i, headline in enumerate(headlines):
        title = headline.find("a")
        # print(subtexts[i].get_text())
        # subtext = subtexts[i].text + subtexts[i].find()
        # subtext = subtexts[i].find("mark", class_="search__highlight")
        # df_row = pd.Series([title.text, subtexts[i].get_text() + subtext.text + subtexts[i].next_sibling.strip()], index=df.columns )
        df_row = pd.Series([title.text, subtexts[i].get_text() ], index=df.columns )

        df = df.append(df_row, ignore_index=True )
    print(df)
    df.to_csv('/Users/nikix/Desktop/a.csv')


if __name__ == '__main__':
    setDefault()
    setElementId()
    search()
    getDataSource(10)
