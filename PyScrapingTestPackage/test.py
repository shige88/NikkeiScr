import time
from selenium import webdriver
import configparser

# Pandas、及び必要なライブラリのインポート
import pandas as pd
from pandas import DataFrame
import numpy as np

# サンプルデータセットを取得する
from sklearn import datasets

# config = configparser.ConfigParser()
# config.read('PyConfig.ini')

# print(config.get('Driver', 'ChromeDriverPath'))

# driver = webdriver.Chrome(config.get('Driver', 'ChromeDriverPath'))
# driver.get('https://www.google.com/')
# time.sleep(5)
# search_box = driver.find_element_by_name("q")
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5)
# driver.quit()
# print("a")
# print("Please input your Nikkei ID>")
# strID = input()
# print("Please input your Nikkei Password>")
# strPass = input()

boston = datasets.load_boston()
# PandasのDataFrame型に変換
df = DataFrame(boston.data, columns = boston.feature_names)
# 目的変数をDataFrameへ追加
df['MEDV'] = np.array(boston.target)
df.head()
