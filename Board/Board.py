from Board.texttable import*

class coordinate:
    def __init__(self,  horizontal, row, col):
        self.__col = col
        self.__row = row
        self.__horizontal = horizontal

    @property
    def row(self):
        return self.__row

    @property
    def col(self):
        return self.__col

    @property
    def horizontal(self):
        return self.__horizontal



class board:
    def __init__(self):
        self.__board = [[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9]

    def __getitem__(self, x):
        return self.__board[x]

    def __setitem__(self, row, col, value):
        self.__board[row][col] = value


    def drawBoard(self):
        t = Texttable()
        d = {0: " ", 1: "X", 2: "#", 3: "B", 4:"C", 5:"D"}
        for i in range(0,8):
            row = self.__board[i][:]
            for j in range(0,8):
                row[j] = d[row[j]]
            row[8] = str(i)
            t.add_row(row)
        for i in range(0,8):
            row[i] = str(i)
        t.add_row(row)
        return t.draw()

    def addBattleship(self, horizontal , row, column):

        if horizontal == 1:
            if column + 4 > 8:
                return True

            elif self.__board[row][column] == self.__board[row][column + 1] == self.__board[row][column + 2] == self.__board[row][column + 3] == 0:
                for index in range(0,4):
                    self.__board[row][column + index] = 3
                return False
            else:

                return True
        elif horizontal == 0:
            if row + 4 > 8:

                return True
            elif self.__board[row][column] == self.__board[row + 1][column] == self.__board[row + 2][column] == \
                self.__board[row + 3][column] == 0:
                self.__board[row][column] = self.__board[row + 1][column] = self.__board[row + 2][column] = \
                self.__board[row + 3][column] = 3
                return False
            else:

                return True
        else:
            return True

    def addCruiser(self, horizontal, row, column):
        if horizontal == 1:
            if column + 3 > 8:
                return True


            elif self.__board[row][column] == self.__board[row][column + 1] == self.__board[row][column + 2] == 0:
                for index in range(0,3):
                    self.__board[row][column + index] = 4
                return False

            else:
                return True

        elif horizontal == 0:
            if row + 3 > 8:

                return True
            elif self.__board[row][column] == self.__board[row + 1][column] == self.__board[row + 2][column] == 0:
                for index in range(0,3):
                    self.__board[row + index][column] = 4
                return False

            else:

                return True
        else:
            return True

    def addDestroyer(self, horizontal, row, column):
        if horizontal == 1:
            if column + 2 > 8:
                return True

            elif self.__board[row][column] == self.__board[row][column + 1] == 0:
                for index in range(0,2):
                    self.__board[row][column + index] = 5
                return False

            else:
                return True

        elif horizontal == 0:
            if row + 2 > 8:
                return True

            elif self.__board[row][column] == self.__board[row + 1][column] == 0:
                for index in range(0,2):
                    self.__board[row + index][column] = 5
                return False

            else:
                return True
        else:
            return True
