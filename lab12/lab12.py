# T-Bike 臺南市公共自行車租賃站資訊
# http://tbike-data.tainan.gov.tw/Service/StationStatus/Json

import requests
import pymysql

r = requests.get("http://tbike-data.tainan.gov.tw/Service/StationStatus/Json", verify=False)  #匯入資料
list_of_dicts = r.json()                                                                      #將資料轉為list格式
a = 0
for i in list_of_dicts:
    print(i["StationName"], i["Address"], i["Capacity"],i["Latitude"],i["Longitude"])
    i["Capacity"] = str(i["Capacity"])
    i["Latitude"] = str(i["Latitude"])
    i["Longitude"] = str(i["Longitude"])
    a = a+1
    if a > 15:
      break 

#資料庫連線設定
db = pymysql.connect(host='localhost', port=3306, user='e94116059', passwd='ethan512tw', db='wordpress', charset='utf8')
#建立操作游標
cursor = db.cursor()
b=0

for i in list_of_dicts:
    sql = "INSERT INTO Tainan_Tbike(StationName, Address, Capacity, Latitude, Longitude) VALUES ('" + i["StationName"] + "','" + i["Address"] + "', '" + i["Capacity"] + "', '" + i["Latitude"] + "', '" + i["Longitude"] + "')"

    try:
      cursor.execute(sql)
      #提交修改
      db.commit()
    except:
      #發生錯誤時停止執行SQL
      db.rollback()
      print('error')

    b = b+1
    if b > 15:
        break

#關閉連線
db.close()