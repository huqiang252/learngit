# -*- coding: utf-8 -*-
import requests
url='https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
lastcommentid=''  #一开始没有上一次的评论
headers={
"Accept":"application/json, text/javascript, */*; q=0.01",
"Origin":"https://y.qq.com",
"Referer":"https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}
for x in range(5):
    params={
    "g_tk":"5381",
    "loginUin":"2649230013",
    "hostUin":"0",
    "format":"json",
    "inCharset":"utf8",
    "outCharset":"GB2312",
    "notice":"0",
    "platform":"yqq.json",
    "needNewCode":"0",
    "cid":"205360772",
    "reqtype":"2",
    "biztype":"1",
    "topid":"102065756",
    "cmd":"8",
    "needmusiccrit":"0",
    "pagenum":str(x),
    "pagesize":"25",
    "lasthotcommentid":lastcommentid,
    "domain":"qq.com",
    "ct":"24",
    "cv":"10101010"
    }

    res=requests.get(url,headers=headers,params=params)
    json_comment=res.json()
    list_comment=json_comment['comment']['commentlist']  #获取到评论列表
    for comment in list_comment:
        print(comment['rootcommentcontent']+'\n\n')
    lastcommentid=list_comment[24]['commentid']
    print('-------------------------------------')