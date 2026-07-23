class TreeNode:
    """definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def numislands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def sink_island_dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return

        grid[r][c] = "0"

        sink_island_dfs(r + 1, c)
        sink_island_dfs(r - 1, c)
        sink_island_dfs(r, c + 1)
        sink_island_dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                sink_island_dfs(r, c)

    return islands
