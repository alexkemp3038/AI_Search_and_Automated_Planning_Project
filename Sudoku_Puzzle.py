
#each cell


#values in the cells
domain = {1,2,3,4,5,6,7,8,9}

#calculate the remaining possible values for each cell
def sudoku_num_calc(cell, sudoku):
    row = cell[0]
    column = cell[1]

    row_values = [sudoku[(row, i)]for i in range(9) if (row, i) in sudoku]
    column_values = [sudoku[(i, column)] for i in range(9) if (i, column) in sudoku]

    box_values = [sudoku[(i,j)] for i in range(row//3*3, row//3*3 + 3) for j in range(column//3*3, column//3*3 +3) if (i,j) in sudoku]

    used_values = [row_values + column_values + box_ values]

    legal_values = domain - used_values
 







