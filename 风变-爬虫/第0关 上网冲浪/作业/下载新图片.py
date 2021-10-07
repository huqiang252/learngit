# -*- coding: utf-8 -*-
import requests
url='https://pics2.baidu.com/feed/9825bc315c6034a8de4c57a4aa4ca851082376ca.jpeg?token=13f97be896ab56c75ceee188512a2457&s=763A33C0D9CC216C467C56120300D0C7'
res=requests.get(url)
#以二进制数据返回
b_text=res.content
with open('摩托罗拉.jpg','wb')  as f_obj:
    f_obj.write(b_text)
