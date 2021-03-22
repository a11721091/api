from util import operationExcel

data = operationExcel.OperationExcel()
line = data.get_lines()
print(line)
i = 3
for num in range(3, 36):
    name_1 = data.get_cell_value(i,10)
    i=i+1
    x = 3
    for num in range(3, 4002):
        name_2 = data.get_cell_value(x, 7)
        line_1 = data.get_cell_value(x,0)
        if name_1 == name_2:

            print(line_1, name_2,name_1)
        x=x+1
