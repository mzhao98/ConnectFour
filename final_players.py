# Name: Michelle Zhao
# CMS cluster login name: mzhao

'''
final_players.py

This module contains code for various bots that play Connect4 at varying 
degrees of sophistication.
'''

import random
from Connect4Simulator import *
# Any other imports go here...


class RandomPlayer:
    '''
    This player makes one of the possible moves on the game board,
    chosen at random.
    '''

    def chooseMove(self, board, player):
        '''
        Given the current board and player number, choose and return a move.

        Arguments:
          board  -- a Connect4Board instance
          player -- either 1 or 2

        Precondition: There must be at least one legal move.
        Invariant: The board state does not change.
        '''

        assert player in [1, 2]
        possibles = board.possibleMoves()
        assert possibles != []
        return random.choice(possibles)


class SimplePlayer:
    '''
    This player will always play a move that gives it a win if there is one.
    Otherwise, it picks a random legal move.
    '''

    def chooseMove(self, board, player):
        '''
        Given the current board and player number, choose and return a move.

        Arguments:
          board  -- a Connect4Board instance
          player -- either 1 or 2

        Precondition: There must be at least one legal move.
        Invariant: The board state does not change.
        '''
        
        #possibles = board.possibleMoves()
        
        #for i in range(0,len(possibles)):
            #if board.isWin(possibles[i]) == True:
                #return possibles[i]
        #return random.choice(possibles)

        
        assert player in [1, 2]
        possibles = board.possibleMoves()
        assert possibles != []
        
        output = -1
        for i in possibles:
            clone = board.clone()
            clone.makeMove(i,player)
            if clone.isWin(i) == True:
                output = i
                
        if output != -1:
            return output
        elif output == -1:
            return random.choice(possibles)  
       
        
    

class BetterPlayer:
    '''
    This player will always play a move that gives it a win if there is one.
    Otherwise, it tries all moves, collects all the moves which don't allow
    the other player to win immediately, and picks one of those at random.
    If there is no such move, it picks a random move.
    '''

    def chooseMove(self, board, player):
        '''
        Given the current board and player number, choose and return a move.

        Arguments:
          board  -- a Connect4Board instance
          player -- either 1 or 2

        Precondition: There must be at least one legal move.
        Invariant: The board state does not change.
        '''
        
        assert player in [1, 2]
        
        opponent = player%2
        if opponent == 0:
            opponent = 2
        possibles = board.possibleMoves()
        assert possibles != []
        goodMove = True
        if len(possibles)==1:
            return possibles[0]
        
        
        for i in possibles:
            clone = board.clone()
            clone.makeMove(i,player)
            if clone.isWin(i) == True:
                return i
        
            for j in possibles:
                clone2 = clone.clone()
                clone2.makeMove(j, opponent)
                if j != i:
                    if clone2.isWin(j) == True:
                        goodMove = False
                        
            if goodMove == True:            
                return i
     
        return random.choice(possibles)
            

class Monty:
    '''
    This player will randomly simulate games for each possible move,
    picking the one that has the highest probability of success.
    '''

    def __init__(self, n, player):
        '''
        Initialize the player using a simpler computer player.

        Arguments: 
          n      -- number of games to simulate.
          player -- the computer player
        '''

        assert n > 0
        self.player = player
        self.n = n

    def chooseMove(self, board, player):
        '''
        Given the current board and player number, choose and return a move.

        Arguments:
          board  -- a Connect4Board instance
          player -- either 1 or 2

        Precondition: There must be at least one legal move.
        Invariant: The board state does not change.
        '''
        
        
        assert player in [1, 2]
        possibles = board.possibleMoves()
        assert possibles != []
        
        opponent = player%2
        if opponent == 0:
            opponent = 2        
 
        for i in possibles:
            clone = board.clone()
            clone.makeMove(i,player)
            if clone.isWin(i) == True:
                return i        
                
        
        p1 = SimplePlayer()
        p2 = SimplePlayer()
        numWins = 0
        highestNumWins = 0
        bestIndex = 0
        for i in possibles:
            clone = board.clone()
            clone.makeMove(i, player)            
            sim = Connect4Simulator(clone, p1, p2, player)
            result = sim.simulate()
            if result == player:
                numWins+=1
            if numWins > highestNumWins:
                highestNumWins = numWins
                bestIndex = i
        return bestIndex
        
