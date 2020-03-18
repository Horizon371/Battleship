
from Board.Board import coordinate

class UI:

    def __init__(self, game):
        self.__game = game

    def readMove(self):
        read = False
        while read == False:
            cord = input("Please enter the coordinates as <<row,column>>: ").split(",")
            row = int(cord[0])
            col = int(cord[1])
            if row >= 0 and row <= 7 and col >=0 and col <= 7:
                return coordinate(1, row, col)
            else:
                print("Coordinates should be in the interval [0,7]")


    def menu(self):

        populate = False
        while populate == False:
            try:
                self.__game.populateComputerBoard()
                self.__game.populatePlayerBoard()
                populate = True
            except Exception as e:
                raise e

        game = True
        while game == True:
            try:
                print("YOUR BOARD")
                print(self.__game.DrawBoard())
                print("\n")
                print("HIT BOARD")
                print(self.__game.DrawHitBoard())
                coord = self.readMove()
                #print(self.__game.DrawComputerBoard())
                print("AI:")
                print(self.__game.DrawComputerHitBoard())
                self.__game.PlayerMove(coord.row, coord.col)
                self.__game.ComputerMove()
                game = self.__game.isMatchOver()
            except Exception:
                print(" ")

