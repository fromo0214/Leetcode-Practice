# https://leetcode.com/problems/word-search/solutions/
def wordSearch(board, word):
    ROWS, COLS = len(board), len(board[0])
    # use a set to add all current values from the board to make sure we don't
    # revisit the same position twice.
    path = set()

    def dfs(row, column, i):
        # if i equals the last postion of word we have reached the word,
        # return true 
        if i == len(word):
            return True
            # out of bounds conditions
        if (row < 0 or column < 0 or row >= ROWS or
            column >= COLS or 
            # if the character we are at is 
            # not equal to the character 
            # we are on the board,              Or what if the position we are at is in path. 
            #                                   means we have visited the same node/position 
            # return false                      twice   
            word[i] != board[row][column]       or (row, column) in path):
                return False
        
        path.add((row, column))
        # check all adjacent positions, running dfs on all 4 adjacent positions
        # If any of these return true we found the character 
        res =   (dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1))
        # cleaning up 
        path.remove((r, c))

    # brute force, go through every position in grid 
    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    
    return False

    # O(n * m * 4^n)
        
        

                


