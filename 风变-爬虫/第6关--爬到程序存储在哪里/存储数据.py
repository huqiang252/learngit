# -*- coding: utf-8 -*-
import requests,xlwt

#定义表存储所有的消息
valuelist=[['歌曲名','所属专辑','播放时长','播放链接']]

#请求，获取，解析数据
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(5):
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.song_next',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x + 1),
        'n': '20',
        'w': '周杰伦',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }

    res_music = requests.get(url, params=params)
    json_music = res_music.json()
    list_music = json_music['data']['song']['list']
    for music in list_music:
        name = music['name']
        # 以name为键，查找歌曲名，把歌曲名赋值给name
        album = music['album']['name']
        # 查找专辑名，把专辑名赋给album
        time = music['interval']
        # 查找播放时长，把时长赋值给time
        link = 'https://y.qq.com/n/yqq/song/' + str(
            music['file']['media_mid']) + '.html'
        # 查找播放链接，把链接赋值给link

        # 把name、album、time和link写成列表，用append函数多行写入Excel
        print('歌曲名：' + name + '\n' + '所属专辑:' + album + '\n' + '播放时长:' + str(
            time) + '\n' + '播放链接:' + link+'\n\n')
        valuelist.append([name,album,time,link])

#存储数据
book=xlwt.Workbook(encoding='utf-8')
sheet=book.add_sheet('歌曲信息')
for i in range(len(valuelist)):
    for j in range(len(valuelist[i])):
        sheet.write(i,j,valuelist[i][j])
book.save('周杰伦歌曲.xls')
