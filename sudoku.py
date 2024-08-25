from pprint import pprint

def find_next_empty(puzzle):
    #finds next row, column that is not yet filled in the puzzle --> rep it with -1
    #return row,column tuple (or None,None),if theres none.
    #keep in mind that were zore indexing from 0 --> 8
    for r in range(9):
        for c in range(9): # range 9 is index 0 --> 9
            if puzzle[r][c] == -1:
                return r,c
    return None, None #if no spaces in the puzzle are empty

def is_valid(puzzle,guess,row,col):
    #figure out if guess at row and column is valid 
    #return true if valid otherwise false
    #lets start with the row
    row_values = puzzle[row]
    if guess in row_values:
        return False #weve repeated and our guess is not valid
    
    #now the columns
    col_values = [puzzle[i][col] for i in range(9)]
    if guess in col_values:
        return False
    #and now the square box that you are in we needto find the 3x3 for the square stats
    #iterate over the 3 values in the row and column
    row_start = (row // 3) * 3 # 9//3 is that 3 will go into 9 3 times without a remainder
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    # if we pass all these conditions we have a valid input
    return True

def solve_sudoku(puzzle):
    #solve sudoku using backtracking
    #our puzzle is a list of lists, which inner list rep a row in our puzzle
    #return whether a soln exists
    #mutates puzzle to be the soln if the soln exists

    # step 1: find a place to make a guess on a puzzle
    row, col = find_next_empty(puzzle)

    #step 1.1: if theres no space left then were done bcs we only accepted valid inputs
    if row is None:
        return True
    
    #if theres a space we need to make a guess btw 1 and 9
    for guess in range(1, 10): #range(1,10) is 1 --> 9
        #step 3: check if it is a valid guess
        if is_valid(puzzle, guess, row, col):
            #step 3.1: if there number is valid then place it on the puzzle at the specific index
            puzzle[row][col] = guess

            #now recurse using this puzzle bcs we need to solve the remaining empty slots
            #recurively call out our function
            if solve_sudoku(puzzle):
                return True
            
        #step 5: if guess is not valid or puzzle not solved we need to back track and reset the invalid input 
        puzzle[row][col] = -1 #resets the guess

    #step 6: if none of the numbers within the range works it means the puzzle is unsolvable
    return False


if __name__ == '__main__':
    example_board = [
        [6, -1, 1,   -1, 7, 2,   4, -1, -1],
        [4, 7, -1,   6, 9, -1,   1, -1, -1],
        [-1, -1, 2,   -1, -1, -1,   -1, -1, -1],

        [5, -1, -1,   8, -1, -1,   -1, 3, -1],
        [-1, 6, -1,   2, 5, 9,   -1, 4, -1],
        [-1, 9, -1,   -1, -1, 7,   -1, -1, 1],

        [-1, -1, -1,   -1, -1, -1,   7, -1, -1],
        [-1, -1, 4,   -1, 8, 5,   -1, 1, 6],
        [-1, -1, 9,   7, 4, -1,   2, -1, 8]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)