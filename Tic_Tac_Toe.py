'''
Created on: Nov 15, 2022
Created by: Nolan Charlton
Purpose of code: A 2 player game of
Tic-Tac-Toe that can end in a win,
a loss, or a draw for both players.
'''
def main():                                         #This function sets the rules of the game and identifies the playing board
    '''
    Arguments
        board: The 3x3 grid on which the game is played
    '''
    print("Let's Play Tic-Tac-Toe! To Enter A Move, Enter The Number That Correlates To The Desired Placement On The Board \n1 2 3 \n4 5 6 \n7 8 9 \nGood Luck!")
          
    board =[['-','-','-'],                          #3x3 grid on which the players will play Tic-Tac-Toe
            ['-','-','-'],
            ['-','-','-']]
    
    printBoard(board)                               #Runs function to print board
    p_1Moves(board)                                 #Runs function for player one's move
    
def p_1Moves(board):                                #This function identifies all the possible player one moves and marks the decided move on the board
    '''
    Arguments
        board: The 3x3 grid on which the game is played
        p1_move: Player one's move input
    Takes
        board variable from main
    Returns
        updates tic-tac-toe board with player one's move
    '''
    p1_move = input("Player One, Enter Your Move")  #This function takes player ones move input
    
    if p1_move == "1":                              #Determines which box the player decided to choose
        board[0][0] = 'X'                           #Replaces that box with an X
        printBoard(board)                           #Runs print board function
        winConditions(board)                        #Runs win conditions function
        p_2Moves(board)                             #Runs player two move function
    elif p1_move == "2":                            #REPEAT
        board[0][1] = 'X'
        printBoard(board)
        winConditions(board)
        p_2Moves(board)
    elif p1_move == "3":                            #REPEAT
        board[0][2] = 'X'
        printBoard(board)
        winConditions(board)
        p_2Moves(board)
    elif p1_move == "4":                            #REPEAT
        board[1][0] = 'X'
        printBoard(board)
        winConditions(board)
        p_2Moves(board)
    elif p1_move == "5":                            #REPEAT
        board[1][1] = 'X'
        printBoard(board)
        winConditions(board)
        p_2Moves(board)
    elif p1_move == "6":                            #REPEAT
        board[1][2] = 'X'
        printBoard(board)
        winConditions(board)
        p_2Moves(board)
    elif p1_move == "7":                            #REPEAT
        board[2][0] = 'X'
        printBoard(board)
        winConditions(board)
        p_2Moves(board)
    elif p1_move == "8":                            #REPEAT
        board[2][1] = 'X'
        printBoard(board)
        winConditions(board)
        p_2Moves(board)
    elif p1_move == "9":                            #REPEAT
        board[2][2] = 'X'   
        printBoard(board)
        winConditions(board)
        p_2Moves(board)      
    elif p1_move != "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":        #Identifies user error
        print("Please Enter An Acceptable Board Value")                                 #Notifies user
        p_1Moves(board)                                                                 #Runs player one move function

def p_2Moves(board):                                #This function takes player twos move input
    '''
    Arguments
        board: The 3x3 grid on which the game is played
        p2_move: Player one's move input
    Takes
        board variable from main
    Returns
        updates tic-tac-toe board with player one's move
    '''
    p2_move = input("Player Two, Enter Your Move")

    if p2_move == "1":                              #Determines which box the player decided to choose
        board[0][0] = 'O'                           #Replaces that box with an X
        printBoard(board)                           #Runs print board function
        winConditions(board)                        #Runs win conditions function
        p_1Moves(board)                             #Runs player two move function
    elif p2_move == "2":                            #REPEAT
        board[0][1] = 'O'
        printBoard(board)
        winConditions(board)
        p_1Moves(board)
    elif p2_move == "3":                            #REPEAT
        board[0][2] = 'O'
        printBoard(board)
        winConditions(board)
        p_1Moves(board)
    elif p2_move == "4":                            #REPEAT
        board[1][0] = 'O'
        printBoard(board)
        winConditions(board)
        p_1Moves(board)
    elif p2_move == "5":                            #REPEAT
        board[1][1] = 'O'
        printBoard(board)
        winConditions(board)
        p_1Moves(board)
    elif p2_move == "6":                            #REPEAT
        board[1][2] = 'O'
        printBoard(board)
        winConditions(board)
        p_1Moves(board)
    elif p2_move == "7":                            #REPEAT
        board[2][0] = 'O'
        printBoard(board)
        winConditions(board)
        p_1Moves(board)
    elif p2_move == "8":                            #REPEAT
        board[2][1] = 'O'
        printBoard(board)
        winConditions(board)
        p_1Moves(board)
    elif p2_move == "9":                            #REPEAT
        board[2][2] = 'O'
        printBoard(board)
        winConditions(board)
        p_1Moves(board)
    elif p2_move != "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":        #Identifies user error
        print("Please Enter An Acceptable Board Value")                                 #Notifies user
        p_2Moves(board)                                                                 #Runs player two move function

def printBoard(board):                              #This function prints the game board
    '''
    Arguments
        board: The 3x3 grid on which the game is played
        row: Horizontal line of values of the 3x3 grid
        col: Vertical line of values on the 3x3 grid
    Takes
        board variable from main
    '''
    for row in range(0,3):                          #Identifies 3 rows
        col = 0                                     #Sets col variable at 0
        for col in range(0,3):                      #Identifies 3 columns
            print(board[row][col], end = " ")       #Prints the board by the number of rows and columns
        print("")  
        
def winConditions(board):                           #This function identifies all possible outcomes to the game
    '''
    Arguments
        board: The 3x3 grid on which the game is played
        play_again: User input on whether or not to run the code again
    Takes
        board variable from main
    '''
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' or board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X' or board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' or board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X' or board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        play_again = input("Player One Is Victorious. Would you like to play again? yes/no")        #If any of the above combinations of filled boxes on the grid are met, player one is declared the victor and prompted to play again
        if play_again == "yes":                     #If player enters yes, they play again
            main()                                  #Runs main function
        elif play_again != "yes":                      #If player enters no, they do not play again
            exit()                                  #Exits the code
    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O' or board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O' or board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O' or board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O' or board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O' or board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O' or board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        play_again = input("Player Two Is Victorious. Would you like to play again? yes/no")        #If any of the above combinations of filled boxes on the grid are met, player two is declared the victor and prompted to play again
        if play_again == "yes":                     #If player enters yes, they play again
            main()                                  #Runs main function
        if play_again != "yes":                      #If player does not enter yes, they do not play again
            exit()                                  #Exits the code
    elif board[0][0] != '-' and board[0][1] != '-' and board[0][2] != '-' and board[1][0] != '-' and board[1][1] != '-' and board[1][2] != '-' and board[2][0] != '-' and board[2][1] != '-' and board[2][2] != '-': 
        play_again = input("Draw. Would you like to play again? yes/no")                            #If any of the above combinations of filled boxes on the grid are met, the game is declared a tie and the players are prompted to play again
        if play_again == "yes":                     #If player enters yes, they play again
            main()                                  #Runs main function
        if play_again != "yes":                      #If player enters no, they do not play again
            exit()                                  #Exits the code

if __name__ == '__main__':
    main()
