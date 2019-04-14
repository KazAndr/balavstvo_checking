# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 22:54:00 2017

@author: Администратор
"""

import xlrd

xl_workbook = xlrd.open_workbook('test.xls',formatting_info=True)

#выбираем активный лист согласно индексу(порядковому номеру)
sheet = xl_workbook.sheet_by_index(0)

#получаем значение первой ячейки A1
val = sheet.row_values(0)[0]
print(val)

#получение списка рабочих листов 
sheet_names = xl_workbook.sheet_names()
print('Sheet Names', sheet_names)

#выбор листа согласно имени
xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])

#получение строки по индексу
row = xl_sheet.row(0)  # 1st row
print(row)


# Вывод всех значение активного листа
#
num_cols = xl_sheet.ncols   # Number of columns
for row_idx in range(0, xl_sheet.nrows):    # Iterate through rows
    print ('-'*40)
    print ('Row: %s' % row_idx)   # Print row number
    for col_idx in range(0, num_cols):  # Iterate through columns
        cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
        print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
        
xl_sheet_2 = xl_workbook.sheet_by_name(sheet_names[1])

num_cols = xl_sheet_2.ncols   # Number of columns
for row_idx in range(0, xl_sheet_2.nrows):    # Iterate through rows
    print ('-'*40)
    print ('Row: %s' % row_idx)   # Print row number
    for col_idx in range(0, num_cols):  # Iterate through columns
        cell_obj = xl_sheet_2.cell(row_idx, col_idx)  # Get cell object by row, col
        print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
#получение цветового индекса        
xfx = xl_sheet_2.cell_xf_index(0, 0)
xf = xl_workbook.xf_list[xfx]
bgx = xf.background.pattern_colour_index
print(bgx)

#получение цветовой карты для определения конкретного цвета по световому индексу
print(xl_workbook.colour_map[bgx])