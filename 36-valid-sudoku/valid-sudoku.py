class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # idea:
        # create dictionary/hashmap for each row, column and 3*3 square 
        # for row and column hashmap, key = index, value = hash set contains all the values appeared so can check for duplication
        # for 3*3 square hashmap, key = (r//3, c//3), value is also hash set like above

        # code:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) 

        for r in range(9):
            for c in range(9):
                # if empty cell, skip
                if board[r][c] == ".": 
                    continue
                # check if number already exists in 3 hash sets (row, col, squares)
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                # add number to 3 hash sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])
        
        return True