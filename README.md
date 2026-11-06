# AI_Search_and_Automated_Planning_Project
<h1>File Structure</h1>
'Sudoku_and_Auto_Planner_Report.pdf' is the report documenting the project - **VIDEO LINK OF RUNTHROUGH IS IN REPORT**.

'GUI_Sudoku_Puzzle' is the GUI for the Sudoku Solver
'Sudoku_Puzzle.py' is the main python script for the Sudoku Solver
'easy.csv' and 'easy.txt' are examples of sudoku files for easy difficulty.
'medium.csv' and 'medium.txt' are examples of sudoku files for medium difficulty.
'hard.csv' and 'hard.txt' are examples of sudoku files for hard difficulty.

'domain.pddl' is the domain file for mission 1 and 2.
'domain-ext.pdd' is the domain file for mission 3. 
'mission1.pddl' and 'mission2.pddl' are problem files which are used to test the original domain file.
'mission3.pddl' is a problem file which is used to test the extended domain file.

<h1>How to Run: Sudoku Solver</h1>
<h2>VSCode</h2>
Open the 'Sudoku_Puzzle.py', and click run on the terminal, Then enter the exact directory path to the sudoku file you wish to test it with.

<h2>Command Prompt</h2>
1. Navigate to the directory 'Sudoku_Puzzle.py' is in by using the 'cd <FILE DIRECTORY>' command. To check if you are in the correct directory, type 'ls' and it should show its name. Then run 'python Sudoku_Puzzle.py' and then type the exact directory path to the sudoku file you wish to test it with.
  
<h1>How to run: Automated Planner</h1>
To run the domain and problem files, run Mission 1 and 2 with domain.pddl and Mission 3 with domain-ext.pddl using a automated planner, such as VSCode's PDDL extension.
