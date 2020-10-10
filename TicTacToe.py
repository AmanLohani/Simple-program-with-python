board = [' ' for x in range(10) ]



def insert_letter(letter,pos):
    board[pos] = letter

def output_board(board):
    print('     |     |     ')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('     |     |     ')
    print('------------------')
    print('     |     |     ')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('     |     |     ')
    print('------------------')
    print('     |     |     ')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('     |     |     ')

def space_free(pos):
    return board[pos] == ' '

def space_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def check_winner(b,l):
    return((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def user_input():
    run = True
    while run:
        move = input("please select a position to enter the X between 1 to 9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')

        except:
            print('Please type a number')


def computer_input():
    possiblemoves = [ x for x ,letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0
    for let in [ 'O', 'X']:
        for i in possiblemoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if check_winner(boardcopy,let):
                move = i
                return move
    cornerspace = []
    for i in possiblemoves:
        for i in [1,3,7,9]:
            cornerspace.append(i)
    if len(cornerspace) > 0 :
        move = select_random(cornerspace)
        return move
    if 5 in possiblemoves:
        move = 5
        return move
    edgespace = []
    for i in possiblemoves:
        for i in [2,4,6,8]:
            edgespace.append(i)
    if len(edgespace)>0:
        move = select_random(edgespace)
        return move

def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def main():
    print("Welcome to the game")
    output_board(board)
    while not space_full(board):
        if not (check_winner(board , 'O')):
            user_input()
            output_board(board)
        else:
            print("Sorry you lost the game!!")
            break

        if not (check_winner(board , 'X')):
            move = computer_input()
            if move == 0:
                print("Tie game")
            else:
                insert_letter('O' , move)
                print("Computer played move at" , move)
                output_board(board)
        else:
            print("You won")
            break

    if space_full(board):
        print("Tie game")

while True:
    x = input("Do you want to play: (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print("-------------------------")
        main()
    else:
        break

