
import requests
import urllib.error
try:
    url="http://www.tipdm.com/"
    r=requests.request("get",url)
    with open("abc.html","w",encoding=r.apparent_encoding) as f:
        f.write(r.text)

except urllib.error.HTTPError as e:
    print(e.reason)
except urllib.error.URLError as e:
    print(e.reason)

