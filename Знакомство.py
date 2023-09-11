import requests


APIKEY = "6aa7183310e1762e5121cc193ab58de5"
params = {"q": "Wroclaw", "appid": APIKEY, "units": "metric"}
headers =  {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru,en;q=0.9",
    "Host": "httpbin.org",
    "Referer": "http://httpbin.org/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-64ef012b-25e66f5d55fa4f414e92c240"
  }
url = "http://httpbin.org/headers"
response = requests.get(url, headers=headers)

# print(response.headers, "headers")
print(response.status_code, "status_code")
# # print(response.request, "request")
print(response.text)
#
# x = response.json()
# print(x["sys"]["country"])
# print(x["name"])
