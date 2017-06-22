from classes import *

global board 
board = [[Tile() for x in range(8)] for y in range(8)]
def setup():
    for x in range(8):
        for y in range(3):
            if((x + y) % 2 == 1):
                piece = Piece(x,y,'B')
                board[x][y].setPiece(piece)
    for x in range(8):
        for y in range(5,8):
            if((x + y) % 2 == 1):
                piece = Piece(x,y,'W')
                board[x][y].setPiece(piece)

def printBoard():
    for y in range(8):
        for x in range(8):
            if(board[x][y].occupier != None):
                print getattr(board[x][y].occupier, 'color'),
            else:
                print " ",
            print "|",
        print ""

def menu():
    print "Checkers babyyyyy"
    print "[1] Start"
    print "[3] Quit"

    choice = raw_input("> ")

    if(choice == '1'):
        start()
    else:
        return

def start():
    setup()
    end = False
    while(not end):
        printBoard()

def askForMove():
    move = raw_input("> ")
    x = translate(move[0])
    y = move[1]

def translate(char):
    char = char.lower()
    ascii_val = ord(char) - 97
    if(ascii_val >= 0 and ascii_val < 26 ):
        return ascii_val
    else:
        return -1

menu()
