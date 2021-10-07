# -*- coding: utf-8 -*-
with open('scores.txt','r',encoding='utf-8') as f_obj:
    contents=f_obj.readlines()

scorelist=[]
dic_data={}
new_dic_data={}
for content in contents:
    datas=content.split()
    sum=0
    for i in datas[1:]:
        sum+=int(i)
    scorelist.append(sum)
    dic_data[sum]=datas[0]

print(dic_data)
scorelist.sort(reverse=True)
print(scorelist)
for i in scorelist:
    if i in dic_data:
        new_dic_data[i]=dic_data[i]
print(new_dic_data)



with open('scores2.txt','w',encoding='utf-8') as f2_obj:
    for i in new_dic_data:
        f2_obj.write(new_dic_data[i]+' '+str(i)+'\n')




