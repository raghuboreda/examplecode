class TicTacToe( object ):
    def __init__( self, n ):
        self.grid = [ [None] *n for i in range(n) ]
        self.size = n

    def move( self, row, col, player ):
        '''
        row is 0 based
        col is 0 based
        player is either 'X' or 'O'
        '''
        self.grid[row][col] = player
        for i in range(self.size):
            for j in range(self.size):
                if j == 0:
                    xcount = 0
                if grid[i][j] == 'X':
                    xcount += 1
                elif grid[i][j] == 'O':
                    ocount += 1
                
