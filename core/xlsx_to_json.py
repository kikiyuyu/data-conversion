# -*- coding: utf-8 -*-
import xlrd
import codecs
import json

#open file
wb = xlrd.open_workbook('../datas/idiom.xlsx')

#获得sheet的namelist
sheet_name_list = wb.sheet_names()

#依次制作数据
for sheet_name in sheet_name_list:
    temp_table = wb.sheet_by_name(sheet_name)
    title_list = temp_table.row_values(0)
    nrows = temp_table.nrows
    temp_dirc = {}
    js = []
    if sheet_name in ('xxx'):
        continue
    print(sheet_name,nrows,title_list)
    for rownum in range(1, nrows):
        rows = temp_table.row_values(rownum)
        temp_dirc = {}
        for colnum in range(0, len(rows)):
            ctype = temp_table.cell(rownum, colnum).ctype
            cell = rows[colnum]
            if ctype == 2 and rows[colnum] % 1 == 0:
                cell = int(cell)
            if ctype == 4:
                cell = True if cell == 1 else False
            # print(title_list(colnum))
            temp_dirc[title_list[colnum]] = cell
        js.append(temp_dirc)
    print(js)
	#输出到文件
    # j = json.dumps(temp_dirc,sort_keys=True, indent=4, separators=(',', ': '))
    file_name = '../datas/%s.json' %sheet_name
    with codecs.open(file_name,"w","utf-8") as f:
        # f.write("var %s =  " %sheet_name )
        f.write(str(js))