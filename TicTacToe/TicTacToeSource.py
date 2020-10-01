import sys

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
i=1
def display_board(board):
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("-----------")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("-----------")
    print(f" {board[1]} | {board[2]} | {board[3]} ")

def check_line(board):
    if(board[7]==board[8]==board[9]!=' '):
        flag=1
        winner=board[7]
        check_flag(flag,winner)
    elif(board[4]==board[5]==board[6]!=' '):
        flag=2
        winner=board[4]
        check_flag(flag,winner)
    elif(board[1]==board[2]==board[3]!=' '):
        flag=3
        winner=board[1]
        check_flag(flag,winner)
    elif(board[7]==board[4]==board[1]!=' '):
        flag=4
        winner=board[7]
        check_flag(flag,winner)
    elif(board[8]==board[5]==board[2]!=' '):
        flag=5
        winner=board[8]
        check_flag(flag,winner)
    elif(board[9]==board[6]==board[3]!=' '):
        flag=6
        winner=board[9]
        check_flag(flag,winner)
    elif(board[1]==board[2]==board[3]!=' '):
        flag=7
        winner=board[1]
        check_flag(flag,winner)
    elif(board[1]==board[5]==board[9]!=' '):
        flag=8
        winner=board[1]
        check_flag(flag,winner)
    elif(board[7]==board[5]==board[3]!=' '):
        flag=9
        winner=board[7]
        check_flag(flag,winner)

def check_flag(flag,winner):
    if flag>0:
        print(f"\nThe winner is {winner} !")
        sys.exit(0)

def starting(i):
    print("Player 1: X")
    print("Player 2: O")
    while(i<9):
        if(i%2==0):
            print("\nEnter the position for Player 1")
            entryPoint=int(input(),10)
            print("\n")
            entry(board,entryPoint,'X')
            display_board(board)
            check_line(board)
            i=i+1
        else:
            print("\nEnter the position for Player 2")
            entryPoint=int(input(),10)
            print("\n")
            i=i+1
            entry(board,entryPoint,'O')
            display_board(board)
            check_line(board)
    if(i==9):
        print("\n")
        display_board(board)
        print("\nIt's a DRAW \n")

def entry(board,entryPoint,val):
    if(board[entryPoint]==' '):
        board[entryPoint]=val
    else:
        print("OVERWRITING. GAME TERMINATED.")
        sys.exit(0)
