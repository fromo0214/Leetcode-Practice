# https://leetcode.com/problems/rotting-oranges/description/

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    for lst in grid:
        print(lst)
    def dfs(r, c, minutes):
        if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1):
            return 
        grid[r][c] += 1
        dfs(r + 1, c, minutes + 1)
        dfs(r - 1, c, minutes + 1)
        dfs(r, c + 1, minutes + 1)
        dfs(r, c - 1, minutes + 1)
    # check to see if there are any oranges with no adjacent neighbors
    minutes = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                dfs(r, c, minutes)
    print()
    for lst in grid:
        print(lst)

    
    return minutes

board = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[2,1,1],[1,1,0],[0,1,1]]
# print(orangesRotting(board))
print(orangesRotting(grid))

