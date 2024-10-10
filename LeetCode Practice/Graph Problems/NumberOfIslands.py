def numOfIslands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or c < 0 or r >= rows or c >= cols
        or grid[r][c] != "1" or (r, c) in visited):
            return

        visited.add((r,c))
        dfs(r + 1, c) 
        dfs(r - 1, c) 
        dfs(r, c + 1) 
        dfs(r, c - 1)


    
    res = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                dfs(r, c)
                res +=1

    return res


print(numOfIslands([["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]))
