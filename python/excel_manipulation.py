# Attendace Checking


from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from datetime import date

# -------

f = open("text/excel_paths.txt")  # To get the path of the file
f_path = f.read()
wb = load_workbook(f_path)        # To load the workbook in the path


Date = date.today()               # To fetch today's date

# To choose an active worksheet
ws = wb.active
ws.title = str(Date)  # To rename the sheet to the date

col = 2  # 1st row is Heading

data_str = ""  # To read from @zeta-bot

l=[]
i = 1
j=1
for i in range(1,6):
    for j in range (1,7):
        try:
            globals() [f'text.{i}.{j}'] = open(f'text.{i}.{j}.txt', 'r')
            globals() [f'var{i}.{j}'] = (globals() [f'text.{i}.{j}']).read()
            print(globals() [f'var{i}.{j}'])
        except FileNotFoundError:
            pass
print("no errors")

for i in l:
    data_str += i


max_rows = ws.max_row

for i in range(max_rows):

    element = ws["A" + str(col)].value  # A1 A2 A3 .....

    if element != None:
        if element in data_str:        # presert condition
            ws["B" + str(col)] = "P"
            ws["B" + str(col)].fill = PatternFill("solid", fgColor="71FF33")

        else:                          # Abscent condition
            ws["B" + str(col)] = "A"   # To mark absent
            ws["B" + str(col)].fill = PatternFill("solid", fgColor="F50707")
        col += 1


wb.save(f_path)    # To save all the changes
