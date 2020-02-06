from bs4 import BeautifulSoup
import requests

# # import urllib.request
# # urllib.request.urlopen("http://daonsup.com/mobile/subpage/sub4-2.asp?v=1&date=2020-02-08")  # url 접속

res = requests.get("http://daonsup.com/mobile/subpage/sub4-2.asp?v=1&date=2020-02-08")  # url 접속
print(res.status_code)
# print(res.text)

source = res.text

soup = BeautifulSoup(source, 'html.parser')      
# print(soup.prettify())



# print(soup.select("#RoomList > tbody"))
top_list = soup.select("#RoomList > tbody")      # 원하는 부분만 선택해서 가져오기
# print(top_list[0].text)in

for top in top_list:
    print(top.text)
# print(soup.p['class'])



# if "예약완료":
#     print("예약가능한 객실이 있습니다.")
