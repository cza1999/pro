# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
header={"user-agent":"Mozilla/5.0"}
prox={"http":"//http://1.1.102:88"}
url="https://zzzttt04.com/"
data=requests.get(url=url,headers=header,timeout=2,proxies=prox)
# data=requests.get(url=url)
data.encoding="utf-8"
print(data.text)
print(data.status_code)
