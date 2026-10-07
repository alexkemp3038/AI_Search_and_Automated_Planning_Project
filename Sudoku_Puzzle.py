
#each cell


#values in the cells
domain = {1,2,3,4,5,6,7,8,9}

#calculate the remaining possible values for each cell
def sudoku_legal_values(cell, sudoku):
    row = cell[0]
    column = cell[1]

    row_values = [sudoku[(row, i)]for i in range(9) if (row, i) != 0]
    column_values = [sudoku[(i, column)] for i in range(9) if (i, column) != 0]

    box_values = [sudoku[(i,j)] for i in range(row//3*3, row//3*3 + 3) for j in range(column//3*3, column//3*3 +3) if (i,j) != 0]

    used_values = set(row_values + column_values + box_values)

    legal_values = domain - used_values

    return legal_values
 







