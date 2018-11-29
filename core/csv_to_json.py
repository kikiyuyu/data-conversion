# -*- coding: utf-8 -*-
import codecs
import json
import csv

#导入目标文件
# wb = xlrd.open_workbook('datas/ball.xlsx')
csv_file = csv.DictReader(open('../datas/idiom.csv','r', encoding="utf-8"))



j = json.dumps(csv_file,sort_keys=True, indent=4, separators=(',', ': '))

file_name = '../datas/idiom.json'
with codecs.open(file_name,"w", "utf-8") as f:
    f.write(j)

# for d in csv_file:
#     # print(d.decode('ascii').encode('utf-8'))
#     print(d)