import os
import csv

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

#calculate the remaining possible values for each cell
def sudoku_num_calc(cell, domain):
    print("hey")


domain = {1,2,3,4,5,6,7,8,9}

# Get file path and extension from user 
filePath, ext = get_filepath()
# Read the Sudoku data from the file
sudokuData = read_sudoku_file(filePath, ext)

# Print the Sudoku data
for row in sudokuData:
    print(row)


