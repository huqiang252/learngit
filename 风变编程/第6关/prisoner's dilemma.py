# -*- coding: utf-8 -*-
#囚徒困境
prisonerList=[]
num=0
while True:
    prisonerDict = {}
    num=num+1
    A=input('囚徒A是认罪还是抵赖:')
    B=input('囚徒B是认罪还是抵赖:')
    prisonerDict['囚徒A'+str(num)]=A
    prisonerDict['囚徒B'+str(num)] = B
    prisonerList.append(prisonerDict)
    if A=='认罪' and B=='认罪':
        print('两人都判10年')
        continue
    if A=='认罪' and B=='抵赖':
        print('囚徒A判1年，囚徒B判20年')
        continue
    if A=='抵赖' and B=='认罪':
        print('囚徒A判20年，囚徒B判1年')
        continue
    if A=='抵赖' and B=='抵赖':
        print('两人都判3年')
        print(prisonerList)
        print('第'+str(len(prisonerList))+'组做出了正确的选择')
        break

for i in range(len(prisonerList)):
    print('第'+str(i+1)+'组的选择是：')
    print('\t'+'囚徒A'+str(i+1)+'选择：'+prisonerList[i]['囚徒A'+str(i+1)])
    print('\t' + '囚徒B'+str(i+1)+'选择：' + prisonerList[i]['囚徒B' + str(i + 1)])