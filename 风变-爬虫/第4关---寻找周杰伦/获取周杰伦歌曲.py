# -*- coding: utf-8 -*-
import requests

url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

for x in range(5):
    params={
        "ct": "24",
        "qqmusic_ver": "1298",
        "new_json": "1",
        "remoteplace": "txt.yqq.song",
        "searchid": "63465533470834920",
        "t": "0",
        "aggr": "1",
        "cr": "1",
        "catZhida": "1",
        "lossless": "0",
        "flag_qc": "0",
        "p": str(x + 1),
        "n": "10",
        "w": "周杰伦",
        "g_tk": "5381",
        "loginUin": "2649230013",
        "hostUin": "0",
        "format": "json",
        "inCharset": "utf8",
        "outCharset": "utf-8",
        "notice": "0",
        "platform": "yqq.json",
        "needNewCode": "0"
    }
    res_music = requests.get(url,params=params)
    json_music = res_music.json() #调用json方法把response对象转化为列表或字典
    list_music=json_music['data']['song']['list'] #list_music是一个列表
    for music in list_music:
        print(music['name'])
        # 以name为键，查找歌曲名
        print('所属专辑：' + music['album']['name'])
        # 查找专辑名
        print('播放时长：' + str(music['interval']) + '秒')
        # 查找播放时长
        print('播放链接：https://y.qq.com/n/yqq/song/' + music['mid'] + '.html\n\n')




