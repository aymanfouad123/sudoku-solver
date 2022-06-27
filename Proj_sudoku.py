#Searches for all empty spaces in the sudoku table 
def find_empty_space(sudokutable):
    for row in range (0,9):
        for col in range (0,9):
            if sudokutable[row][col] == 0:
                return row , col
    return None , None #If no spaces are empty return None, i.e, table has been solved.

#Checks if the guess is valid to be in the row and column
def val_checker(sudokutable,guess,row ,col):

    #Checking the row 
    rowfinval = sudokutable[row]
    if guess in rowfinval:
        return False  

    #Checking the column 
    colfinval = []
    for c in range (0,9):
        colfinval += [sudokutable[c][col]]
    if guess in colfinval:
        return False

    #Checking the subsquares 
    rowstartval = (row // 3) * 3
    colstartval = (col // 3) * 3 
    for ro in range (0,3):
        for co in range (0,3):
            if sudokutable[rowstartval + ro][colstartval + co] == guess:
                return False 
    return True 


#Main function
def sudoku_solver(sudokutable):
    row , col = find_empty_space(sudokutable)
    if row is None :
        sudoku_visual(sudokutable)
        return True 
    for guess in range (1,10):
        if val_checker(sudokutable,guess,row,col) == True:
            sudokutable[row][col] = guess 
            if sudoku_solver(sudokutable):
                return True 
        sudokutable[row][col] = 0
    return False 

#This function prints the sudoku table
def sudoku_visual(sudokutable):
    for row in sudokutable:
        for ele in row:
	    print(ele)
	print('\n')
	
#Code Run
s = [[0,0,7, 0,0,0, 0,1,5], [0,0,0, 3,9,7, 0,0,0], [0,6,2, 0,1,0, 4,0,9],[0,2,0, 0,0,1, 5,4,3],[7,0,0, 4,0,9, 0,0,1], [4,8,1, 2,0,0, 0,6,0], [9,0,6, 0,2,0, 7,3,0], [0,0,0, 9,8,4, 0,0,0],[1,5,0, 0,0,0, 2,0,0]]
print(sudoku_solver(s))
print(s)









