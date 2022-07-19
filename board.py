from cell import Cell

class Board:
    def __init__(self):
        self.cells = [][]

    def createTicTacToeBoard(self):
        for row in range(3):
            for col in range(3):
                self.cells[row][col] = Cell()
    
    def analyseResult(self , row = 0 , col = 0 , count = 1 , prevSymbol = "Z"):
        if count == 3:
            print("Game Over")
            return
        elif row > 2 or col > 2:
            return
        elif self.cells[row][col] == prevSymbol:
            self.analyzeResult(row + 1 , col + 1 , count + 1 , self.cells[row][col])
            self.analyzeResult(row , col + 1 , count + 1 , self.cells[row][col])
            self.analyzeResult(row + 1 , col , count + 1 , self.cells[row][col])
        else:
            self.analyzeResult(row + 1 , col + 1 ,  1 , self.cells[row][col])
            self.analyzeResult(row , col + 1 , 1 , self.cells[row][col])
            self.analyzeResult(row + 1 , col , 1 , self.cells[row][col])

    def printBoard(self):
        print(self.cells[0][0] + " " + self.cells[0][1] + " " + self.cells[0][2])
        print(self.cells[1][0] + " " + self.cells[1][1] + " " + self.cells[1][2])
        print(self.cells[2][0] + " " + self.cells[2][1] + " " + self.cells[2][2])