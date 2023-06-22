"""
    0-island_perimeter module
"""


def island_perimeter(grid):
    """
     arg(grid): a list of integers
     Returns: perimeter of island
    """

    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 sides to the perimeter

                # Check if neighboring cells are also land
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for each adjacent land cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 for each adjacent land cell

    return perimeter
