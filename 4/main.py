def isValid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def checkDiagonal(grid, x, y, dx1, dy1, dx2, dy2, n, m):
    """
    Check if two diagonals form "MAS" or "SAM" relative to the center.
    """
    # First diagonal
    x1, y1 = x + dx1, y + dy1
    x2, y2 = x - dx1, y - dy1

    # Second diagonal
    x3, y3 = x + dx2, y + dy2
    x4, y4 = x - dx2, y - dy2

    # Ensure all positions are within bounds
    if all(
        isValid(xi, yi, n, m) for xi, yi in [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    ):
        diagonal1 = grid[x1][y1] + grid[x][y] + grid[x2][y2]
        diagonal2 = grid[x3][y3] + grid[x][y] + grid[x4][y4]

        # Check if each diagonal contains "MAS" or "SAM"
        return sorted(diagonal1) == ["A", "M", "S"] and sorted(diagonal2) == [
            "A",
            "M",
            "S",
        ]
    return False


def countXMASPatterns(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0

    diagonals = [
        ((1, 1), (1, -1)),  # Top-left to bottom-right, Top-right to bottom-left
    ]

    for x in range(n):
        for y in range(m):
            if grid[x][y] == "A":  # Center of an X
                for (dx1, dy1), (dx2, dy2) in diagonals:
                    if checkDiagonal(grid, x, y, dx1, dy1, dx2, dy2, n, m):
                        count += 1

    return count


def main():
    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file.readlines()]

    result = countXMASPatterns(grid)
    print(result)


if __name__ == "__main__":
    main()
