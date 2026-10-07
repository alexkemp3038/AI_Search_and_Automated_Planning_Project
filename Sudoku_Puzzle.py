
#each cell
cell
sudoku


#values in the cells
domain = {1,2,3,4,5,6,7,8,9}

#calculate the remaining possible values for each cell
def sudoku_legal_values(cell, sudoku):
    row = cell[0]
    column = cell[1]

    row_values = [sudoku[(row, i)]for i in range(9) if sudoku[(row, i)]!= 0]
    
    column_values = [sudoku[(i, column)] for i in range(9) if sudoku[(i, column)] != 0]

    box_values = [sudoku[(i,j)] for i in range(row//3*3, row//3*3 + 3) for j in range(column//3*3, column//3*3 +3) if sudoku[(i,j)] != 0]

    used_values = set(row_values + column_values + box_values)

    legal_values = domain - used_values

    return legal_values




def solve_sudoku(sudoku):
    
    def num_of_legal_values(cell):
        return len(sudoku_legal_values(cell, sudoku))
    
    
    
    empty_cells = [(i,j) for i in range(9) for j in range(9) if sudoku[(i,j)] == 0]

    if not empty_cells:
        return True

    cell = min(empty_cells, key = num_of_legal_values)

    legal_values = sudoku_legal_values(cell, sudoku)


    for value in legal_values:
        sudoku[cell] = value
        if solve_sudoku(sudoku):
            return True

        sudoku[cell] = 0

    return False

        

    

 







