# Attendace Checking


from openpyxl import load_workbook         #importing openpyxl(module used to work on excel sheets)
from openpyxl.styles import PatternFill           #option to colour
from datetime import date                       #importing date and time

# -------

f = open("text/excel_paths.txt")  # To get the path of the file
f_path = f.read()
wb = load_workbook(f_path)        # To load the workbook in the path


Date = date.today()               # To fetch today's date

   
ws = wb.active           # To choose an active worksheet   
ws.title = str(Date)           # To rename the sheet to the date

col = 2  # 1st row is Heading

data_str = ""  # To read from @zeta-bot

l=[]
i = 1
j=1
for i in range(1,6):
    for j in range (1,8):
        try:
            globals() [f'text.{i}.{j}'] = open(f'text.{i}.{j}.txt', 'r')          #TEXT FILE HAVING NAMES OF ALL STUDENTS
            globals() [f'var{i}.{j}'] = (globals() [f'text.{i}.{j}']).read()
            l.append(globals() [f'var{i}.{j}'])
        except FileNotFoundError:
            pass
print("no errors")

for i in l:
    data_str += i


max_rows = ws.max_row

for i in range(max_rows):

    element = ws["A" + str(col)].value  # A1 A2 A3 .....(column names)

    if element != None:
        if element.lower() in data_str.lower():        # presert condition
            ws["B" + str(col)] = "P"
            ws["B" + str(col)].fill = PatternFill("solid", fgColor="71FF33")    #colouring the sheet with green beside respective name

        else:                          # Abscent condition
            ws["B" + str(col)] = "A"   # To mark absent
            ws["B" + str(col)].fill = PatternFill("solid", fgColor="F50707")      #to colour red
        col += 1


wb.save(f_path)    # To save all the changes
