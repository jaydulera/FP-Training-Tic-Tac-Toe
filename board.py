from cell import Cell

class Board:
    def __init__(self):
        self.cells = [ [Cell() , Cell() , Cell()] for i in range(3)]


    def createTicTacToeBoard(self):
        for row in range(0 , 3):
            for col in range(0 , 3):
                self.cells[row][col] = Cell()
    
    def analyseResult(self):
        victory , victorSymbol = self.checkHorizontal()
        # print("Horizontal" , victory)
        if victory:
            return True , victorSymbol
        else:
            victory , victorSymbol = self.checkVertical()
            # print("Vertical" , victory)
            if victory:
                return True , victorSymbol
            else:
                victory , victorSymbol = self.checkDiagonal()
                # print("Diagonal" , victory)
                if victory:
                    return True , victorSymbol
                else:
                    return False , None
            
  

    def checkHorizontal(self):
        for row in range(3):
            if self.cells[row][0].symbol == self.cells[row][1].symbol and self.cells[row][1].symbol == self.cells[row][2].symbol and self.cells[row][0].symbol != "*":
                return True , self.cells[row][0].symbol
        return False , None
    
    def checkVertical(self):
        for col in range(3):
            if self.cells[0][col].symbol == self.cells[1][col].symbol and self.cells[1][col].symbol == self.cells[2][col].symbol and self.cells[1][col].symbol != "*":
                return True , self.cells[0][col].symbol
        return False , None

    def checkDiagonal(self):
        if self.cells[0][0].symbol == self.cells[1][1].symbol and self.cells[1][1].symbol == self.cells[2][2].symbol and self.cells[1][1].symbol != "*": 
            return True , self.cells[1][1].symbol
        if self.cells[0][2].symbol == self.cells[1][1].symbol and self.cells[1][1].symbol == self.cells[2][0].symbol and self.cells[1][1].symbol != "*": 
            return True , self.cells[1][1].symbol
        return False , None


    def printBoard(self):
        # print(self.cells[0][0])
        # print("{} {} {}".format(self.cells[0][0] , self.cells[0][1] , self.cells[0][2]))
        # print("{} {} {}".format(self.cells[1][0] , self.cells[1][1] , self.cells[1][2]))
        # print("{} {} {}".format(self.cells[2][0] , self.cells[2][1] , self.cells[2][2]))
        print(self.cells[0][0].symbol + " | " + self.cells[0][1].symbol + " | " + self.cells[0][2].symbol)
        print("----------")
        print(self.cells[1][0].symbol + " | " + self.cells[1][1].symbol + " | " + self.cells[1][2].symbol)
        print("----------")
        print(self.cells[2][0].symbol + " | " + self.cells[2][1].symbol + " | " + self.cells[2][2].symbol)