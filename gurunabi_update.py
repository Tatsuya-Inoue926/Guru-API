import csv
import datetime
import requests
import pprint

url = "https://api.gnavi.co.jp/RestSearchAPI/v3/"

nam = input("フリーワードを入力してください。ワードとワードの間には,を付けてください")

params = {}
params["keyid"] = "KEYID"
#keyidは個人で異なる
params["freeword"] = nam

response = requests.get(url, params)
#print(response)

#pprint.pprint(response.json())
results = response.json()

restaurants = results["rest"]

csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = ("gurunabi" + nam + "data" + csv_date + ".csv")
f = open(csv_file_name, "w", encoding="cp932", errors="ignore")

writer = csv.writer(f, lineterminator="\n") 
csv_header = ["店名","住所","営業時間","定休日","電話番号","URL"]
writer.writerow(csv_header)

for g in restaurants:
    print( g["name"], g["address"], g["opentime"], g["holiday"], g["tel"], g["url"])
    csvlist = []
    csvlist.append(g["name"])
    csvlist.append(g["address"])
    csvlist.append(g["opentime"])
    csvlist.append(g["holiday"])
    csvlist.append(g["tel"])
    csvlist.append(g["url"])
    writer.writerow(csvlist)
f.close()
