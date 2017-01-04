# Name: Michelle Zhao
# CMS cluster login name: mzhao

'''
final_board.py

This module contains classes that implement the Connect-4 board object.
'''

# Imports go here...
import copy

class MoveError(Exception):
    '''
    Instances of this class are exceptions which are raised when
    an invalid move is made.
    '''
    pass

class BoardError(Exception):
    '''
    Instances of this class are exceptions which are raised when
    some erroneous condition relating to a Connect-Four board occurs.
    '''
    pass

class Connect4Board:
    '''
    Instance of this class manage a Connect-Four board, but do not
    manage the play of the game itself.
    '''

    def __init__(self):
        '''
        Initialize the board.
        '''
        self.board = []
        for i in range(0,6):
            self.board.append([0]*7)
       
        
        
 

    def getRows(self):
        '''
        Return the number of rows.
        '''
        rows = len(self.board)
        return rows
     
    def getCols(self):
        '''
        Return the number of columns.
        '''
        cols = len(self.board[0])
        return cols


    def get(self, row, col):
        '''
        Arguments:
          row -- a valid row index
          col -- a valid column index

        Return value: the board value at (row, col).

        Raise a BoardError exception if the 'row' or 'col' value is invalid.
        '''
        if row < 0 or row >= self.getRows():
            raise BoardError('row index out of range')
        if col < 0 or col >= self.getCols():
            raise BoardError('column index out of range')        
        
        val = self.board[row][col]
        return val

    def clone(self):
        '''
        Return a clone of this board i.e. a new instance of this class
        such that changing the fields of the new instance will not
        affect the old instance.

        Return value: the new Connect4Board instance.
        '''    
        clone = copy.deepcopy(self)
        return clone

    def possibleMoves(self):
        '''
        Compute the list of possible moves (i.e. a list of column numbers 
        corresponding to the columns which are not completely filled up).

        Return value: the list of possible moves
        '''
        list_possible = []
        for i in range(0, 7):
            if self.board[5][i] == 0:
                list_possible.append(i)
        return list_possible
   
   
    def makeMove(self, col, player):
        '''
        Make a move on the specified column for the specified player.

        Arguments:
          col    -- a valid column index
          player -- either 1 or 2

        Return value: none

        Raise a MoveError exception if a move cannot be made because the column
        is filled up, or if the column index or player number is invalid.
        '''
        if col < 0 or col >= 7:
            raise MoveError('column index out of range')   
        if player != 1 and player != 2:
            raise MoveError('player number invalid')          
        list_possible = self.possibleMoves()
        if self.board[5][col] !=0:
            raise MoveError('move not possible')             
        
        board_clone = self.clone()
        
        row = 0
        for i in range(0, 6):
            if self.board[i][col] == 0:
                row = i
                break
            
        self.board[row][col] = player


    def unmakeMove(self, col):
        '''
        Unmake the last move made on the specified column.

        Arguments:
          col -- a valid column index

        Return value: none

        Raise a MoveError exception if there is no move to unmake, or if the
        column index is invalid.
        '''
        if col < 0 or col >= 7:
            raise MoveError('column index out of range')           
        if self.board[0][col]==0:
            raise MoveError('no move to unmake')
        
               
        row = 0
        for i in range(5, -1, -1):
            if self.board[i][col] != 0:
                row = i
                break
        self.board[row][col] = 0

    def isHorizontalWin(self, col, row, player):
        winCount = 0
        isHorizontalWin = False
        col_index = col
        while col_index>=0:
            if self.board[row][col_index] == player:
                winCount += 1
            if self.board[row][col_index] != player:
                col_index = col+1
                break
            col_index -= 1
            
        while col_index<7:
            if self.board[row][col_index] != player:
                            break            
            if self.board[row][col_index] == player:
                winCount += 1
            
            col_index += 1 
            
        if winCount == 4:
            isHorizontalWin = True
        return isHorizontalWin

  
    def isVerticalWin(self, col, row, player):
        winCount = 0
        isVerticalWin = False
        row_index = row
        while row_index>=0:
            if self.board[row_index][col] == player:
                winCount += 1
            if self.board[row_index][col] != player:
                row_index = row+1
                break
            row_index -= 1
            
        while row_index<6:
            if self.board[row_index][col] == player:
                winCount += 1        
            if self.board[row_index][col] != player:
                break
            row_index += 1    
            
        if winCount == 4:
            isVerticalWin = True
        return isVerticalWin

  
    def isUpDiagonalWin(self, col, row, player):
        winCount = 0
        isDiagonalWin = False
        row_index = row
        col_index = col
        while row_index>=0 and col_index>=0:
            if self.board[row_index][col_index] == player:
                winCount += 1
            if self.board[row_index][col_index] != player:
                break
            row_index -= 1
            col_index -= 1            
        
        row_index = row+1
        col_index = col+1        
        while row_index < 6 and col_index < 7:
            if self.board[row_index][col_index] == player:
                winCount += 1
            if self.board[row_index][col] != player:
                break
            row_index += 1  
            col_index += 1  
            
        if winCount == 4:
            isDiagonalWin = True
        return isDiagonalWin
  
    def isDownDiagonalWin(self, col, row, player):
        winCount = 0
        isDiagonalWin = False
        row_index = row
        col_index = col
        while row_index<6 and col_index>=0:
            if self.board[row_index][col_index] == player:
                winCount += 1
            if self.board[row_index][col_index] != player:
                break
            row_index += 1
            col_index -= 1            
            
        row_index = row-1
        col_index = col+1        
        while row_index>=0 and col_index<7:
            if self.board[row_index][col_index] == player:
                winCount += 1
            if self.board[row_index][col_index] != player:
                break
            row_index -= 1  
            col_index += 1  
            
        if winCount == 4:
            isDiagonalWin = True
        return isDiagonalWin



    def isWin(self, col):
        '''
        Check to see if the last move played in column 'col' resulted in a win
        (four or more discs of the same color in a row in any direction).

        Argument: 
          col    -- a valid column index

        Return value: True if there is a win, else False

        Raise a BoardError exception if the column is empty (i.e. no move has
        ever been made in the column), or if the column index is invalid.
        '''
        isWin = False
        if col < 0 or col >= 7:
            raise BoardError('column index out of range')  
        if self.board[0][col] == 0:
            raise BoardError('no player in column')          
       
        row = 0
        player = 0
        for i in range(5, -1, -1):
            if self.board[i][col] != 0:
                row = i
                player = self.board[i][col]
                break
        
        
        if self.isHorizontalWin(col, row, player) == True:
            isWin = True 
    
        if self.isVerticalWin(col, row, player) == True:
            isWin = True    

        if self.isDownDiagonalWin(col, row, player) == True:
            isWin = True  
 
        if self.isUpDiagonalWin(col, row, player) == True:
            isWin = True    

        return isWin


  

    def isDraw(self):
        '''
        Check to see if the board is a draw because there are no more
        columns to play in.

        Precondition: This assumes that there is no win on the board.

        Return value: True if there is a draw, else False
        '''
        isDraw = False
        list_possible = self.possibleMoves()
        if len(list_possible) == 0:
            isDraw = True
        return isDraw

    def isWinningMove(self, col, player):
        '''
        Check to see if making the move 'col' by the player 'player'
        would result in a win.  The board state does not change.

        Arguments:
          col    -- a valid column index
          player -- either 1 or 2

        Return value: True if the move would result in a win, else False.

        Precondition: This assumes that the move can be made.
        '''
        isWinningMove = False
        self.makeMove(col, player)
        if self.isWin(col) == True:
            isWinningMove = True
        return isWinningMove


    def isDrawingMove(self, col, player):
        '''
        Check to see if making the move 'col' by the player 'player'
        would result in a draw.  The board state does not change.

        Arguments:
          col    -- a valid column index
          player -- either 1 or 2

        Return value: True if the move would result in a draw, else False.

        Precondition: This assumes that the move can be made, and that the
        move has been checked to see that it does not result in a win.
        '''
        isDrawingMove = False
        self.makeMove(col, player)
        if self.isDraw() == True:
            isDrawingMove = True
        return isDrawingMove
