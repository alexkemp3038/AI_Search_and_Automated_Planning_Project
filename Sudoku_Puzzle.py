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

# Checks if the number to be inserted (k) is valid within the given grid, row and column
def is_valid(grid, r, c, k):
    # To be valid, it needs to pass 3 constraints:
    
    # 1. The number is not already in the row
    rowCheck = k not in grid[r]

    # 2. The number is not already in the column
    columnCheck = k not in [grid[i][c] for i in range(9)]

    # 3. The number is not already in the 3x3 box
    boxCheck = k not in [grid[i][j] for i in range(r//3*3, r//3*3 + 3) for j in range(c//3*3, c//3*3 + 3)]

    # Will return:
        # True if the number is valid
        # False if the number is not valid
    return rowCheck and columnCheck and boxCheck

#calculate the remaining possible values for each cell
def sudoku_num_calc(cell, sudoku):
    row = cell[0]
    column = cell[1]

    row_values = [sudoku[(row, i)]for i in range(9) if (row, i) in sudoku]
    column_values = [sudoku[(i, column)] for i in range(9) if (i, column) in sudoku]

    box_values = [sudoku[(i,j)] for i in range(row//3*3, row//3*3 + 3) for j in range(column//3*3, column//3*3 +3) if (i,j) in sudoku]

    used_values = [row_values + column_values + box_ values]

    legal_values = domain - used_values

# Solves the Sudoku puzzle using recursive backtracking
def solve(grid, r=1, c=1):
    # Base case: If r is 10, we have filled all the rows, so solution is found.
    if r == 10:
        return True

    # If c is 10, we have completed the row so we move to the next row.
    elif c == 10:
        return solve(grid, r + 1, 1)

    # If the cell is already filled, we move to the next column.
    elif grid[r-1][c-1] != 0:
        return solve(grid, r, c + 1)

    # If the cell is empty, we try to fill it with numbers from 1 to 9.
    else:
        for k in range(1, 10):
            # Check if the number is valid
            if is_valid(grid, r, c, k):
                # If valid, we place the number in the cell
                grid[r-1][c-1] = k

                # Recursively try to solve the rest of the grid, moving to the next cell
                if solve(grid, r, c + 1):
                    return True

                # If it doesn't lead to a solution, we reset the cell and try the next number
                grid[r-1][c-1] = 0

        # If we have tried all numbers and none worked, we return False to backtrack 
        return False

# Get file path and extension from user 
filePath, ext = get_filepath()
# Read the Sudoku data from the file
sudokuData = read_sudoku_file(filePath, ext)

# Print the Sudoku data
for row in sudokuData:
    print(row)

# Solve the Sudoku puzzle
solve(sudokuData)


