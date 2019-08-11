from collections import defaultdict
def findWords( board, words):
    '''
    type board: List[List[str]]
    type words: List[str]
    rtype: List[str]
    words = ["oath", "pea", "eat", "ragin"]
    boards = [['o','a','a','n'], 
              ['e','t','a','e'],
              ['i','h','k','r'],
              ['i','f','l','v']
              ]
    output = ["eat", "oath"]
    Given a 2D board and list of words in the dictionary find all words in the board
    Each word must be constructed from letters of sequentially adjacent cells
    where adjacent cell are those horizontal or vertical neighbors.
    same cell may not be used more than once in a word.
    '''
    if board is None:
        return []
    rowM = len(board)
    colM = len(board[0])
    adjL = [(0,1),(0,-1),(1,0),(-1,0)]
    result = []

    def recHelper(w, nw, i, j, seen=None):
        seen[(i,j)] = 1
        if w == nw:
            result.append(w)
            return
        if len(w) == len(nw):
            return
        for ni, nj in adjL:
            if i+ni < 0 or i+ni >= rowM:
                continue
            if j+nj < 0 or j+nj >= colM:
                continue
            if seen[(i+ni,j+nj)] > 0:
                continue
            if len(nw) == 8:
                print  'after seen', i+ni, j+nj
            if board[i+ni][j+nj] == w[len(nw)]:
                recHelper(w, nw+w[len(nw)], i+ni, j+nj, seen)
        seen[(i,j)] = 0
 
    keen = defaultdict(int)
    for word in words:
        for ir in range(rowM):
            for jr in range(colM):
                if word[0] == board[ir][jr]:
                    recHelper(word, word[0], ir, jr, seen=keen)

    return result

words = ["eaabcdgfa"]
boards = [['a','b','c'], 
          ['a','e','d'],
          ['a','f','g'],
         ]

l = findWords( boards, words)
print l

