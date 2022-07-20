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
        # self.turn = 1

    def createGame(self):
        # self.board.createTicTacToeBoard()
        self.move(row = int(input('Enter row: ')) , col = int(input('Enter column: ')))

    def play(self , row , col , symbol):
        if row < 0 or col < 0 or row > 2 or col > 2:
            print("Invalid cell")
        elif self.board.cells[row][col].isMarked():
            print("Cell already filled")
        else:
            self.board.cells[row][col].symbol = symbol

    def move(self , row , col , symbol = "X"):
        flag = False
        self.play(row , col , symbol)
        self.board.printBoard()
        while(flag == False):
            if(symbol == "X"):
                symbol = "O"
            else:
                symbol = "X"
            self.play(row = int(input('Enter row: ')) , col = int(input('Enter column: ')) , symbol = symbol)
            self.board.printBoard()
            flag , victorSymbol = self.board.analyseResult()
        if flag:
            print("Victor is " , victorSymbol)
        else:
            print("It's a draw")

if __name__ == "__main__":
    game1 = Game('jay' , 'jash')
    game1.createGame()


