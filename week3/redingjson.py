# 定義了在複雜世界中幫助開啟URLs (主要是HTTP )的函式和類——基本和摘要認證、重定向、cookies等等，這個模組主要負責構造和發起網路請求
import urllib.request as request
import json
import ssl
import csv
ssl._create_default_https_context = ssl._create_unverified_context
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with request.urlopen(src) as response:  # 開啟網頁
    data = json.load(response)
    final_list = []
    result_data = data["result"]["results"]
    for i in result_data:
        if i["xpostDate"][0:4] >= "2015":  # 找出年份大於等於2015
            list = []
            stitle = i["stitle"]  # 找出景點名稱
            list.append(stitle)
            address = i["address"][5:8]  # 找出地區
            list.append(address)
            longitude = round(float(i["longitude"]), 4)  # 找出經緯度並四捨五入至小數點後四位
            list.append(longitude)
            latitude = round(float(i["latitude"]), 4)
            list.append(latitude)
            file = i["file"].lower()  # 先將所有http網址變成.jpg
            file_1 = file.split(".jpg")[0]
            file_2 = file_1+".jpg"  # 找出第一筆資料
            list.append(file_2)

            final_list.append(list)  # 將串接好資料加入list

    print(final_list)

    with open("data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(final_list)
