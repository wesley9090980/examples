from re import S
import xlrd
from xlrd import sheet
import xlwt

#读取文件
book=xlrd.open_workbook('20年数据.xlsx')
sheet=book.sheet_by_index(0)

sheets=book.sheets()
sheetnames=book.sheet_names()

s=sheet.row_values(0)
s2=sheet.col_values(0)

cell=sheet.cell(0,0)
cell.value='sjflsj'


print(cell.value)

#写文件
xlwt.Workbook()
sheet.write(0,0,'hello')
book.save("ttt.xlsx")