def pathUtil( i, j, rL, cL, strList, board, p):
    if i == rL or j == cL:
        return
    p = p + board[i][j]
    if i == rL-1 and j == cL-1:
        strList.append(p)
        return
    pathUtil( i, j+1, rL, cL, strList, board, p)
    pathUtil( i+1, j, rL, cL, strList, board, p)

def pathPrints( board ):
    rL = len(board)
    cL = len(board[0])
    strList = []
    p = ''
    pathUtil(0, 0, rL, cL, strList, board, p)
    return strList

sl = pathPrints( [['A','X', 'E'], ['B', 'Y', 'F'], ['C','D','R']] )
print sl
