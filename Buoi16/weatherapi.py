import requests

url = "http://api.openweathermap.org/data/2.5/weather?q="
city = input("Nhap vao thanh pho: ")
api_key = 'fe53bfd100e8ca1c2ca47f202a2e9b9c'

url_getapi = url + city + "&appid=" + api_key

#Vi du: Muon lay API cua Ha Noi
# http://api.openweathermap.org/data/2.5/weather?q=seoul&appid=fe53bfd100e8ca1c2ca47f202a2e9b9c

data = requests.get(url_getapi).json()
# print(data)
if data['cod'] == '404':
    print("Khong tim thay thanh pho")
else:
    print(data)
    print(data['weather'])
    print(data['main']['temp_min'])
    print(data['main']['temp_max'])