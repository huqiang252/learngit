# -*- coding: utf-8 -*-
import requests,xlwt

url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
valuelist=[['文章标题','文章简介','文章链接']]


headers={
"referer":"https://www.zhihu.com/people/zhang-jia-wei/posts/posts_by_votes?page=1",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}
x=0
while True:
    if x > 2:
        break
    params={
    "include":"data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics",
    "offset":str(x*20),
    "limit":"20",
    "sort_by":"voteups"
    }
    res=requests.get(url=url,params=params,headers=headers)
    # print(res.status_code)
    json_connect=res.json()
    list_connect=json_connect['data']
    is_end=json_connect['paging']['is_end']
    # if is_end==True:
    #     tag=False #设置标记为False 循环结束

    for connect in list_connect:
        my_title=connect['title'] #获取文章标题
        my_excerpt=connect['excerpt'] #获取文章简介
        my_url=connect['url']
        # print(my_title+'\n'+my_excerpt+'\n'+my_url+'\n\n')
        valuelist.append([my_title,my_excerpt,my_url])
    x = x + 1  # 表明循环一次，页数加1


#存储数据
book=xlwt.Workbook(encoding='utf-8')
sheet=book.add_sheet('Sheet1')

for i in range(len(valuelist)):
    for j in range(len(valuelist[i])):
        sheet.write(i,j,valuelist[i][j])

book.save('知乎大v张佳玮.xlsx')
