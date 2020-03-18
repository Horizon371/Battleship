import unittest
from Board.Board import *
from Game.Game import *

class test(unittest.TestCase):
    def setUp(self):
        self.__game = game()
        self.__board = board()

    def test_board(self):
        self.__board = [[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9]
        self.assertEqual(self.__board, [[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9,[0]*9])

    def test_game(self):
        pass
