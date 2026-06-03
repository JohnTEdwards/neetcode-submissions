from collections import defaultdict as dd
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #
        rows = dd(set)
        cols = dd(set)
        squares = dd(set)

        for r in range(9): # board is 9 x 9
            for c in range(9):
                currBoardPosition = board[r][c]
                if currBoardPosition == '.': #base case skip loop
                    continue
                #check for invalid positions
                if (currBoardPosition in rows[r] 
                    or currBoardPosition in cols[c]
                    or currBoardPosition in squares[(r//3,c//3)]):
                    return False
                #else append to hashmap
                rows[r].add(currBoardPosition)
                cols[c].add(currBoardPosition)
                squares[(r//3, c//3)].add(currBoardPosition)
        return True