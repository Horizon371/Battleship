from AI.AI import *



class game:

    row = 0
    col = 0
    def __init__(self):
        self.__board = board()
        self.__computerBoard = board()
        self.__hitBoard = board()
        self.__computerHitBoard = board()
        self.__AI = AI(self.__computerHitBoard)
        self.__playerHitCount = 0
        self.__computerHitCount = 0
        self.__ComputerBattleshipHit = 0
        self.__ComputerCruiserHit = 0
        self.__ComputerDestroyerHit = 0
        self.__BattleshipHit = 0
        self.__CruiserHit = 0
        self.__DestroyerHit = 0



    @staticmethod
    def UIAddShip():

        print(" ")
        horizontal = None
        while horizontal == None:
            command = input("Do you want to add on horizontal?" + "\n" + "1: YES   2: NO" + "\n" + "Enter command: ")
            if command == "1":
                horizontal = 1
            elif command == "2":
                horizontal = 0
            else:
                print("Invalid command!")

        if horizontal == 1:
            pos = False
            while pos == False:
                try:
                    position = input("Please enter the starting position as <<row,column>>" + "\n"
                                 + "The squares will be completed from the position to the right: ").split(",")
                    if len(position)!= 2:
                        raise ValueError
                    row = int(position[0])
                    column = int(position[1])
                    pos = True
                except ValueError as v:
                    print(str(v))




        elif horizontal == 0:
            pos = False
            while pos == False:
                try:
                    position = input("Please enter the starting position as <<row,column>>" +
                                     "\n" + "The squares will be completed from the position downwards: ").split(",")
                    if len(position)!= 2:
                        raise ValueError
                    row = int(position[0])
                    column = int(position[1])
                    pos = True
                except ValueError as v:
                    print(str(v))

        return coordinate(horizontal, row, column)

    def populatePlayerBoard(self):

        test = True
        while test == True:
            print("\n")
            print("\n")
            print("\n")
            print(self.__board.drawBoard())
            print("ADD BATTLESHIP: ")
            coord = self.UIAddShip()
            test = self.__board.addBattleship(coord.horizontal, coord.row, coord.col)
            if test == True:
                print("Not enough space")

        test1 = True
        while test1 == True:
            try:
                print("\n")
                print("\n")
                print("\n")
                print(self.__board.drawBoard())
                print("ADD CRUISER: ")
                coord = self.UIAddShip()
                test1 = self.__board.addCruiser(coord.horizontal, coord.row, coord.col)
                if test1 == True:
                    print("Not enough space")
            except Exception:
                test1 = True

        test2 = True
        while test2 == True:
            print("\n")
            print("\n")
            print("\n")
            print(self.__board.drawBoard())
            print("ADD DESTROYER: ")
            coord = self.UIAddShip()
            test2 = self.__board.addDestroyer(coord.horizontal, coord.row, coord.col)
            if test2 == True:
                print("Not enough space")

        return False


    def populateComputerBoard(self):

        test = True
        while test == True:
            coord = AI.randomPopulatorBatleship()
            test = self.__computerBoard.addBattleship(coord.horizontal, coord.row, coord.col)

        test1 = True
        while test1 == True:
            coord = AI.randomPopulatorCruiser()
            test1 = self.__computerBoard.addCruiser(coord.horizontal, coord.row, coord.col)

        test2 = True
        while test2 == True:
            coord = AI.randomPopulatorDestroyer()
            test2 = self.__computerBoard.addDestroyer(coord.horizontal, coord.row, coord.col)

        return False

    def DrawBoard(self):
        return self.__board.drawBoard()

    def DrawComputerBoard(self):
        return self.__computerBoard.drawBoard()

    def DrawHitBoard(self):
        return self.__hitBoard.drawBoard()

    def DrawComputerHitBoard(self):
        return self.__computerHitBoard.drawBoard()

    def PlayerMove(self,row,column):
        if self.__computerBoard[row][column] == 3:
            self.__hitBoard[row][column] = 3
            self.__BattleshipHit += 1
            print("Battleship hit")
        elif self.__computerBoard[row][column] == 4:
            self.__hitBoard[row][column] = 4
            self.__CruiserHit += 1
            print("Cruiser hit")
        elif self.__computerBoard[row][column] == 5:
            self.__hitBoard[row][column] = 5
            self.__DestroyerHit += 1
            print("Destroyer hit")
        else:
            self.__hitBoard[row][column] = 1

    def ComputerMove(self):
        coord = self.__AI.generateMove(self.__ComputerDestroyerHit, self.__ComputerBattleshipHit, self.__ComputerCruiserHit, self.row, self.col)
        #print(self.__ComputerBattleshipHit)
        row = coord.row
        column = coord.col
        #print(row," ----- ",column)

        if self.__board[row][column] == 3:
            self.__computerHitBoard[row][column] = 3
            self.__ComputerBattleshipHit += 1
            self.row = row
            self.col = column
        elif self.__board[row][column] == 4:
            self.__computerHitBoard[row][column] = 4
            self.__ComputerCruiserHit += 1
            self.row = row
            self.col = column
        elif self.__board[row][column] == 5:
            self.__computerHitBoard[row][column] = 5
            self.__ComputerDestroyerHit += 1
            self.row = row
            self.col = column
        else:
            self.__computerHitBoard[row][column] = 1
        if self.__board[row][column] != 0:
            self.__board[row][column] = 2

    def isMatchOver(self):

        if self.__BattleshipHit + self.__DestroyerHit + self.__CruiserHit == 9:
            print("PLAYER WINS!")
            return False

        elif self.__ComputerBattleshipHit + self.__ComputerCruiserHit + self.__ComputerDestroyerHit == 9:
            print("COMPUTER WINS!")
            print(self.__computerBoard.drawBoard())
            return False

        elif self.__BattleshipHit == 4:
            print("Battleship destroyed")
        elif self.__DestroyerHit == 2:
            print("Destroyer destroyed lol")
        elif self.__CruiserHit == 3:
            print("Cruiser destroyed")
        return True
