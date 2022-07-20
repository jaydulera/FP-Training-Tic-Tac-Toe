class Cell:
    def __init__(self , symbol = "*"):
        self.symbol = symbol

    def isMarked(self):
        if self.symbol == "X" or self.symbol == "O":
            return True
        else:
            return False    