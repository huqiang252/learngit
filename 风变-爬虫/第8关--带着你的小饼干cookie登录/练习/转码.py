# -*- coding: utf-8 -*-
from urllib import parse
data={'username':'demo100','password':'demo200'}
postdata=parse.urlencode(data).encode('utf-8')
print(postdata)
print(type(postdata))