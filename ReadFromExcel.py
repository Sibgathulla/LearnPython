import xlrd
import os.path

wb = xlrd.open_workbook(os.path.join('D:\TRB 2014 Data','SPS1 demo data.xlsx'))
wb.sheet_names()
sh = wb.sheet_by_index(0)
i = 1
with open("Output.txt", "a") as my_file:
    while sh.cell(i,11).value != 0:
        Load = sh.cell(i,11).value
        all_d = sh.col_values(i, 13, 19)
        DB1 = Load + " " + (" ".join(all_d))
        my_file.write(DB1 + '\n')
        i += 1
