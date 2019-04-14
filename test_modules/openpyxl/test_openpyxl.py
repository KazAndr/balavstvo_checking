# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 18:50:49 2017

@author: Администратор
"""

import openpyxl

wb = openpyxl.load_workbook("test.xlsx", data_only=True)
print(wb.get_sheet_names())
print()
sheet = wb.get_sheet_by_name('0')
print(len(list(sheet.rows)[0]))

rows = sheet.rows
values = []

for row in rows:
    for cell in row:
        values.append(cell.value)
        
print(values)
cell = 'A2'
try:
    print(sheet[cell].fill.start_color.index[2:])
except:
    Colors = openpyxl.styles.colors.COLOR_INDEX
    print(Colors[sheet[cell].fill.start_color.index])
