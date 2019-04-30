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
import time
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import sys
import time
import os

args = sys.argv
root_query = input("キーワードを入力してください: ")

browser = webdriver.Chrome(os.getcwd() + "/chromedriver.exe")

columns = ["root_query", "branch_query", "query_name"]
df = pd.DataFrame(columns=columns)

browser.get('https://www.google.co.jp/search?num=100&q=' + root_query)
time.sleep(1)
tags = browser.find_elements_by_css_selector("p.nVcaUb")
print (tags)
related_words = []
counter = 0

for tag in tags:
branch_query = tag.text
print (branch_query)
related_words.append(branch_query)
se = pd.Series([root_query, branch_query,branch_query ], columns)
df = df.append(se, ignore_index=True)

related_words_num = len(related_words)
print (str(related_words_num) + "件関連キーワードを取得しました")
print (related_words)
counter = 1

for related_word in related_words:
print (str(counter) + "/" + str(related_words_num))
browser.get('https://www.google.co.jp/search?num=10&q=' + related_word)
second_tags = browser.find_elements_by_css_selector("p.nVcaUb")
for tag in second_tags:
branch_query = tag.text
print (branch_query)
se = pd.Series([related_word, branch_query,branch_query], columns)
df = df.append(se, ignore_index=True)
counter+=1
time.sleep(3)

df.to_csv(root_query + ".csv")
print ("CSVに出力しました")