import pytest
from cell import Cell

newCell = Cell()
def testOne():
    newCell.symbol = None
    assert newCell.isMarked() == False
def testTwo():
    newCell.symbol = "X"
    assert newCell.isMarked() == True
def testThree():
    newCell.symbol = "O"
    assert newCell.isMarked() == True
def testFour():
    newCell.symbol = "random"
    assert newCell.isMarked() == False
