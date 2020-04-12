import requests
import urllib.error
try:
    r=requests.get("https://www.xgmn.org/hasjdk.html")
    # print(r.encoding)
    # print(r.apparent_encoding)

    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text)
except urllib.error.URLError as e:
    print(e)