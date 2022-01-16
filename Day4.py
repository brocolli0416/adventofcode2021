import numpy as np

def lookforbingo(board): # Check if a board contains a bingo row or column
        for i in range(0, 4):
            if (board[:, i] == ['X']).all():
                return True
            if (board[i, :] == ['X']).all():
                return True
        else:
            return False

with open('day4.txt', 'r') as dat:
    ############
    ## Part I ##
    ############
    ### Preparation ###
    game_orig = dat.read().split('\n\n')
    game_orig[-1] = game_orig[-1][:-1]
    numbers = list(game_orig[0].split(','))
    numbers = [int(i) for i in numbers]
    print(numbers)
    boards = game_orig[1:]
    #print(boards[0])
    n_boards = []
    nn_boards = []
    for i in boards:
        n_boards.append(list(i.split('\n')))
    #print(n_boards[len(nn_boards)-1])
    for board in n_boards:
        board = [list(row.split(' ')) for row in board]
        n_board = []
        for nrow in board:
            if nrow == []:
                print('empty row')
                board.remove(nrow)
            nrow = [int(j) for j in nrow if j != '']
            n_board.append(nrow)
        n_board = np.array(n_board, dtype=object)
        nn_boards.append(n_board)

    ### Play Bingo ###
    # Go through each number, mark the called number in the board. Find out which board gets a BINGO first
    # Go through each board, replace the called number with 'X'. Check if the board has a row of X or a column of X.
    # If there's a bingo, check which board it is and what number has been just called. Calculate the score: sum(all unmarked number)*called number.

    def playbingo(numbers, nn_boards):
        for callnumber in numbers:
            for c, board in enumerate(nn_boards):
                if (callnumber == board).any():
                    nn_boards[c] = np.where(board == callnumber, 'X', board)
                    if lookforbingo(nn_boards[c]) == True:
                        print('BINGO')
                        return callnumber, nn_boards[c]

    # callnum, winningboard = playbingo(numbers, nn_boards)
    # print(callnum, winningboard)
    # winningboard = list(winningboard.flat)
    # boardscore = [i for i in winningboard if i != 'X']
    # print(sum(boardscore)*callnum)

    #############
    ## Part II ##
    #############
    numberofboards = len(nn_boards)
    def playbingo2(numbers, nn_boards):
        win = 0
        completeboard = np.array([[9999]*5]*5)
        for callnumber in numbers:
            for c, board in enumerate(nn_boards):
                if (callnumber == board).any():
                    nn_boards[c] = np.where(board == callnumber, 'X', board)
                    if lookforbingo(nn_boards[c]) == True:
                        original = nn_boards[c]
                        nn_boards[c] = completeboard
                        win += 1
                        
                    if win == numberofboards:
                        return callnumber, original


        

    callnum, losingboard = playbingo2(numbers, nn_boards)
    print(callnum, losingboard)
    losingboard = list(losingboard.flat)
    boardscore = [i for i in losingboard if i != 'X']
    print(sum(boardscore)*callnum)                  

   
    
    