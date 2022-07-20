import pytest
from board import Board

newBoard = Board()
newBoard.createTicTacToeBoard()

def testVictory():
    newBoard.cells[0][0].mark = "X"
    newBoard.cells[0][1].mark = "X"
    newBoard.cells[0][2].mark = "X"
    newBoard.cells[1][0].mark = "O"
    newBoard.cells[1][1].mark = "O"
    newBoard.cells[1][2].mark = "O"
    newBoard.cells[2][0].mark = "O"
    newBoard.cells[2][1].mark = "O"
    newBoard.cells[2][2].mark = "O"
    newBoard.printBoard()
    victory , victorSymbol = newBoard.analyseResult()

    assert victory == True

def testDraw():
    newBoard.cells[0][0].mark = "X"
    newBoard.cells[0][1].mark = "X"
    newBoard.cells[0][2].mark = "0"
    newBoard.cells[1][0].mark = "O"
    newBoard.cells[1][1].mark = "O"
    newBoard.cells[1][2].mark = "X"
    newBoard.cells[2][0].mark = "X"
    newBoard.cells[2][1].mark = "X"
    newBoard.cells[2][2].mark = "O"
    newBoard.printBoard()
    victory , victorSymbol = newBoard.analyseResult()

    assert victory == False
