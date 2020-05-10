# Program to extract number of
# columns in Python
import xlrd
import xlwt
# import xlsxwriter module
import xlsxwriter



loc = ("Tilt-5.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)


# Extracting number of columns
print(sheet.ncols)

workbook = xlsxwriter.Workbook('t5.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0

for i in range(sheet.nrows):
    if ( " 10:00" in sheet.cell_value(i, 1)):
        content = sheet.row_values(i)
        c=0
        for item in content:
            # write operation perform
            worksheet.write(row, column+c, item)
            c += 1
            #print(item)
            # incrementing the value of row by one
            # with each iteratons.
        row += 1



workbook.close()









