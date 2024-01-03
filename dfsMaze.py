def is_valid_move(maze, row, col, visited):
    # Check if the move is within the maze boundaries and is not a wall or already visited
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0 and not visited[row][col]

def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(row, col):
        # Base case: reached the bottom-right corner
        if row == rows - 1 and col == cols - 1:
            visited[row][col] = True
            return True

        # Mark the current cell as visited
        visited[row][col] = True

        # Define possible moves: up, down, left, right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = row + move[0], col + move[1]
            if is_valid_move(maze, new_row, new_col, visited):
                if dfs(new_row, new_col):
                    return True

        # If no valid moves, backtrack by marking the cell as unvisited
        visited[row][col] = False
        return False

    # Start DFS from the top-left corner
    if dfs(0, 0):
        print("Path found:")
        for row in visited:
            print(row)
    else:
        print("No path found.")

# Example maze (0 represents an open path, 1 represents a wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

solve_maze(maze)
