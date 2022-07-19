from player import Player
from board import Board

"""
1 2 3
4 5 6
7 8 9
"""

class Game:
    def __init__(self , nameOne , nameTwo):
        self.player1 = Player(nameOne , "X")
        self.player2 = Player(nameOne , "O")
        self.board = Board()
        self.turn = 1

    def createGame(self):
        self.board.createTicTacToeBoard()
        self.move(row = input() , col = input())

    def play(self , row , col , symbol):
        if row < 0 or col < 0 or row > 2 or col > 2:
            print("Invalid move")
        elif self.board.cells[row][col]:
            print("Invalid move")
        else:
            self.board.cells[row][col] = symbol

    def move(self , row , col , symbol = "X"):
        while(True):
            self.play(row , col , symbol)
            if(symbol == "X"):
                symbol = "O"
            else:
                symbol = "X"
            self.move(row = input() , col = input() , symbol = symbol)
            self.board.analyseResult()
            self.board.printBoard()

