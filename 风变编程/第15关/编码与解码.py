# -*- coding: utf-8 -*-
print('吴枫'.encode('utf-8'))
print('吴枫'.encode('gbk'))
print(b'\xe5\x90\xb4\xe6\x9e\xab'.decode('utf-8'))
print(b'\xce\xe2\xb7\xe3'.decode('gbk'))

print(type('吴枫'))
print(type(b'\xce\xe2\xb7\xe3'))

print(b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'.decode('utf-8')) #我爱你

print('K'.encode('ASCII')) #b'K'
