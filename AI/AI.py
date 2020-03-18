import random
from Board.Board import*

class AI:

    seekBattleship = 0
    seekCruiser = 0
    seekDestroyer = 0
    rowCoord = 0
    colCoord = 0
    up = 0
    down = 0
    left = 0
    right = 0

    def __init__(self, enemyBoard):
        self.__enemyBoard = enemyBoard

    @staticmethod
    def randomPopulatorBatleship():

        horizontal = random.randint(0,1)
        if horizontal == 1:
            row = random.randint(0,7)
            column = random.randint(0, 3)
        else:
            row = random.randint(0, 3)
            column = random.randint(0, 7)
        return coordinate(horizontal, row, column)

    @staticmethod
    def randomPopulatorCruiser():
        horizontal = random.randint(0, 1)
        if horizontal == 1:
            row = random.randint(0, 7)
            column = random.randint(0, 4)
        else:
            row = random.randint(0, 4)
            column = random.randint(0, 7)
        return coordinate(horizontal, row, column)

    @staticmethod
    def randomPopulatorDestroyer():
        horizontal = random.randint(0, 1)
        if horizontal == 1:
            row = random.randint(0, 7)
            column = random.randint(0, 5)
        else:
            row = random.randint(0, 5)
            column = random.randint(0, 7)
        return coordinate(horizontal, row, column)

    def generateRandomMove(self):
        generated = False
        while generated == False:
            row = random.randint(0, 7)
            col = random.randint(0, 7)
            if row % 2 == 0 and col % 2 == 1 and self.__enemyBoard[row][col] == 0:
                generated = True
            elif row % 2 == 1 and col % 2 == 0 and self.__enemyBoard[row][col] == 0:
                generated = True

        return coordinate(1, row, col)

    def resetDirections(self):
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0

    def generateMove(self, DestroyerHit, BattleshipHit, CruiserHit, row, col):

        if self.__enemyBoard[row][col] == 3:
            self.seekBattleship = 1

        elif self.__enemyBoard[row][col] == 4:
            self.seekCruiser = 1

        elif self.__enemyBoard[row][col] == 5:
            self.seekDestroyer = 1

        if DestroyerHit == 2:
            self.seekDestroyer = 0
        if BattleshipHit == 4:
            self.seekBattleship = 0
        if CruiserHit == 3:
            self.seekCruiser = 0

        if self.left == 1:
            self.resetDirections()
            return coordinate(1, row, col - 1)

        if self.right == 1:
            self.resetDirections()
            return coordinate(1, row, col + 1)

        if self.up == 1:
            self.resetDirections()
            return coordinate(1, row + 1, col)

        if self.down == 1:
            self.resetDirections()
            return coordinate(1, row - 1, col)

        if self.seekBattleship == self.seekCruiser == self.seekDestroyer == 0:
            self.resetDirections()
            return self.generateRandomMove()

        if row <= 6 and self.__enemyBoard[row + 1][col] == 0:
            self.resetDirections()
            return coordinate(1, row + 1, col)

        elif row >= 1 and self.__enemyBoard[row - 1][col] == 0 and self.__enemyBoard[row + 1][col] == 1:
            self.resetDirections()
            return coordinate(1, row - 1, col)

        elif col <= 6 and self.__enemyBoard[row][col + 1] == 0:
            self.resetDirections()
            return coordinate(1, row, col + 1)

        elif col >= 1 and self.__enemyBoard[row][col - 1] == 0 and self.__enemyBoard[row][col + 1] == 1:
            self.resetDirections()
            return coordinate(1, row, col - 1)

        elif self.__enemyBoard[row + 1][col] == 1:
            self.left = 1
            for i in range(col, col - 4, -1):
                if self.__enemyBoard[row][i] == 0:
                    return coordinate(1, row, i)

        elif self.__enemyBoard[row - 1][col] == 1:
            self.right = 1
            for i in range(col, col + 4):
                if self.__enemyBoard[row][i] == 0:
                    return coordinate(1, row, i)

        elif self.__enemyBoard[row][col + 1] == 1:
            self.down = 1
            for i in range (row, row - 4, -1):
                if self.__enemyBoard[i][col] == 0:
                    return coordinate(1, i, col)

        elif self.__enemyBoard[row][col - 1] == 1:
            self.down = 1
            for i in range(row, row + 4):
                if self.__enemyBoard[i][col] == 0:
                    return coordinate(1, i, col)
        else:
            self.resetDirections()
            return self.generateRandomMove()





