# Using Depth-First Search (DFS) to trace the path of a word in a 2D grid
def trace_word_path(word, grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)] 

    def dfs(r, c, idx, path, visited):
        if idx == len(word):
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in visited and grid[nr][nc] == word[idx]):
                result = dfs(nr, nc, idx + 1, path + [[nr, nc]], visited | {(nr, nc)})
                if result:
                    return result
        return None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:
                result = dfs(r, c, 1, [[r, c]], {(r, c)})
                if result:
                    return result
    return "Not present"

grid = [
  ["B", "I", "T", "R"],
  ["I", "U", "A", "S"],
  ["S", "C", "V", "W"],
  ["D", "O", "N", "E"]
]

print(trace_word_path("BISCUIT", grid)) 