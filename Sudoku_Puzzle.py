import os, csv

#Takes a name for a sudoku file
def get_filepath():
    while True:
        filePath = input("Please enter the file path of the sudoku file (.txt or .csv): ")

        #Check if file exists
        if not os.path.exists(filePath):
            print("File not found. Please try again.")
            continue

        #Extract extension
        _, ext = os.path.splitext(filePath)
        ext = ext.lower()

        #Check if the file extension is valid
        if ext in ['.txt', '.csv']:
            return filePath, ext
        else:   
            print("Invalid file type. Please enter a .txt or .csv file.")

# Reads the sudoku data from a file and returns it as a list of lists
def read_sudoku_file(filePath, ext):
    sudokuData = []

    # Opens file contents
    with open(filePath, 'r') as file:
        # If file is a .txt file
        if ext == '.txt':
            # Read each line in the file
            for line in file:
                # Remove whitespace
                line = line.strip()
                # Skips empty lines
                if line:
                    sudokuData.append([int(num) for num in line.split()])

        # If file is a .csv file
        elif ext == '.csv':
            # Use csv.reader to read the file
            reader = csv.reader(file)
            # Read each line in the CSV file
            for line in reader:
                # Skips empty lines
                if line:
                    # If the line is not empty, convert the numbers to integers
                    sudokuData.append([int(num) for num in line])

    return sudokuData


#values in the cells
domain = {1,2,3,4,5,6,7,8,9}

def is_valid_file(sudokuData):
    if len(sudokuData) != 9:
        return False
    
    for row in sudokuData:
        if len(row) !=9 :
            return False
        
        for value in row:
            if value not in domain and value != 0:
                return False
    
    return True

def is_valid_sudoku(grid):
    # To be valid, it needs to pass 3 constraints:
    for r in range(9):
        for c in range(9):
            k = grid[r][c]

        if k == 0:
            continue
    # 1. The number is not already in the row
        rowCheck = k not in grid[r]

    # 2. The number is not already in the column
        columnCheck = k not in [grid[i][c] for i in range(9)]

    # 3. The number is not already in the 3x3 box
        boxCheck = k not in [grid[i][j] for i in range(r//3*3, r//3*3 + 3) for j in range(c//3*3, c//3*3 + 3)]

    # Will return:
        # True if the number is valid
        # False if the number is not valid
        if not (rowCheck and columnCheck and boxCheck):
            return False

    return True
  

    

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

def convert_sudoku_to_dict(sudokuData):
    sudoku = {}
    for i in range(9):
        for j in range(9):
            sudoku[(i,j)] = sudoku[i][j]

    return sudoku

def print_sudoku(sudoku):
    for i in range(9):
        if i % 3 == 0:
            print("------------------------")

    for j in range(9):
        if j %3 == 0:
            print("|", end = " ")

        print(sudoku[(i,j)], end = " ")

    print("|")

print("------------------------")







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




filePath, ext = get_filepath()

sudokuData = read_sudoku_file(filePath, ext)

if not is_valid_file(sudokuData):
    print("Invalid Sudoku file!")

elif not is_valid_sudoku(sudokuData):
    print ("Invalid Sudoku puzzle!")

else:


    sudoku = convert_sudoku_to_dict(sudokuData)

    if solve_sudoku(sudoku):
        print("Sudoku succesfully solved!")
        print_sudoku(sudoku)
    
    else:
        print("No solution can be found")

    

        

    

 







