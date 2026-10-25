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

# finds if the given sudoku file is suitable to be used
def is_valid_file(sudokuData):
    #check there is 9 rows
    if len(sudokuData) != 9:
        return False

    #check that each row has 9 values
    for row in sudokuData:
        if len(row) !=9 :
            return False

        #check that each value is in the domain
        for value in row:
            if value not in domain and value != 0:
                return False
    
    return True

#finds if the given sudoku puzzle is valid 
def is_valid_sudoku(grid):
    # To be valid, it needs to pass 3 constraints:
    for r in range(9):
        for c in range(9):
            k = grid[r][c]

            if k == 0:
                continue

        #initalise the cell to 0 so it doesnt count itself
            grid[r][c] = 0
    
    # 1. The number is not already in the row
            rowCheck = k not in grid[r]

    # 2. The number is not already in the column
            columnCheck = k not in [grid[i][c] for i in range(9)]

    # 3. The number is not already in the 3x3 box
            boxCheck = k not in [grid[i][j] for i in range(r//3*3, r//3*3 + 3) for j in range(c//3*3, c//3*3 + 3)]

        #4. Restore the orignal value of the cell
            grid[r][c] = k

    # Will return:
        # True if the number is valid
        # False if the number is not valid
            if not (rowCheck and columnCheck and boxCheck):
                print("Invalid number:", k)
                print("Position:", r, c)
                print("Row check:", rowCheck)
                print("Column check:", columnCheck)
                print("Box check:", boxCheck)
                return False

    return True
  

    

#calculate the remaining possible values for each cell
def sudoku_legal_values(cell, sudoku):

    #extra the row and column coords from the cell tuple
    row = cell[0]
    column = cell[1]

    #get the values already in the row
    row_values = [sudoku[(row, i)]for i in range(9) if sudoku[(row, i)]!= 0]

    #get the values already in the column
    column_values = [sudoku[(i, column)] for i in range(9) if sudoku[(i, column)] != 0]

    #get the values already in the 3x3 box
    box_values = [sudoku[(i,j)] for i in range(row//3*3, row//3*3 + 3) for j in range(column//3*3, column//3*3 +3) if sudoku[(i,j)] != 0]

    #combine all the used values
    used_values = set(row_values + column_values + box_values)

    #find the legal values remaining 
    legal_values = domain - used_values

    return legal_values

#converts the sudoku data into a dictionary, where each cell is represented by its coords (row, column)
def convert_sudoku_to_dict(sudokuData):
    #create empty dictionary
    sudoku = {}

    #fil the dictionary by iterating through the sudoku data
    for i in range(9):
        for j in range(9):
            sudoku[(i,j)] = sudokuData[i][j]

    return sudoku

#prints the sudoku puzzle in a readable format similar to how its shown in general sudoku puzzles
def print_sudoku(sudoku):

    #print a horizontal line every 3 rows
    for i in range(9):
        if i % 3 == 0:
            print("------------------------")
        
        #print a vertical line every 3 columns
        for j in range(9):
            if j %3 == 0:
                print("|", end = " ")

            #print the value of the current cell
            print(sudoku[(i,j)], end = " ")

        #print end vertical line
        print("|")

    #print bottom horizontal line
    print("------------------------")






#solving algorithm for the sudoku puzzle using backtracking search with the MRV heuristic
def solve_sudoku(sudoku):

    #helper function counts the number of legal values available for current cell
    def num_of_legal_values(cell):
        return len(sudoku_legal_values(cell, sudoku))
    
    
    #find all the empty cells in the sudoku puzzle
    empty_cells = [(i,j) for i in range(9) for j in range(9) if sudoku[(i,j)] == 0]

    #base case: if there are no empty cells, the puzzle is solved
    if not empty_cells:
        return True

    #select the next cell with the minimum number of legal values(MRV)
    cell = min(empty_cells, key = num_of_legal_values)

    #get the legal values for the current cell
    legal_values = sudoku_legal_values(cell, sudoku)

    #try each legal value for the current cell
    for value in legal_values:
        sudoku[cell] = value
        
        #recursively call to solve the sudoku
        if solve_sudoku(sudoku):
            return True

        #backtrack if the current value does not work
        sudoku[cell] = 0

    return False





#---------MAIN PROGRAM---------

#get the file path and extension from user
filePath, ext = get_filepath()

#read sudoku data from file
sudokuData = read_sudoku_file(filePath, ext)

#check if the file is valid
if not is_valid_file(sudokuData):
    print("Invalid Sudoku file!")

#check if the puzzle is valid
elif not is_valid_sudoku(sudokuData):
    print ("Invalid Sudoku puzzle!")

else:

    #convert sudoku data into dictionary format 
    sudoku = convert_sudoku_to_dict(sudokuData)

    #print the solved sudoku puzzle
    if solve_sudoku(sudoku):
        print("Sudoku succesfully solved!")
        print_sudoku(sudoku)
    
    else:
        print("No solution can be found")

    

        

    

 







