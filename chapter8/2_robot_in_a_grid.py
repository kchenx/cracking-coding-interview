# Robot in a Grid
# Imagine a robot sitting on the upper left corner of grid with r rows and
# c columns. The robot can only move in two directions, right and down, but
# certain cells are "off limits" such that the robot cannot step on them.
# Design an algorithm to find a path for the robot from the top left to
# the bottom right.

from typing import Dict, List, Tuple
import unittest

# f(i, j) =     [(i, j)],               (i, j) = (0, 0)
#               null,                   grid[i][j] is blocked/off the board
#               f(i-1, j) + [(i, j)],   f(i-1, j) != null
#               f(i, j-1) + [(i, j)],   f(i, j-1) != null


def find_path_recursive(grid: List[List[bool]],
                        i: int = None, j: int = None) -> List[Tuple[int, int]]:
    if i is None:
        i = len(grid) - 1
    if j is None:
        j = len(grid[0]) - 1

    if is_out_of_bounds(grid, i, j) or not grid[i][j]:
        return None

    if i == 0 and j == 0:
        return [(i, j)]

    uppath = find_path_recursive(grid, i-1, j)
    if uppath:
        uppath.append((i, j))
        return uppath

    downpath = find_path_recursive(grid, i, j-1)
    if downpath:
        downpath.append((i, j))
        return downpath

    return None


def find_path_memo(grid: List[List[bool]], i: int = None, j: int = None,
                   memo: Dict[Tuple[int, int], List[Tuple[int, int]]] = None) -> List[Tuple[int, int]]:
    if i is None:
        i = len(grid) - 1
    if j is None:
        j = len(grid[0]) - 1

    if is_out_of_bounds(grid, i, j) or not grid[i][j]:
        return None

    if i == 0 and j == 0:
        return [(i, j)]

    if memo is None:
        memo = {}

    if (i-1, j) not in memo:
        memo[(i-1, j)] = find_path_memo(grid, i-1, j, memo)

    uppath = memo[(i-1, j)]
    if uppath:
        uppath.append((i, j))
        return uppath

    if (i, j-1) not in memo:
        memo[(i, j-1)] = find_path_memo(grid, i, j-1, memo)

    leftpath = memo[(i, j-1)]
    if leftpath:
        leftpath.append((i, j))
        return leftpath

    return None


def is_out_of_bounds(grid: List[List[bool]], i: int, j: int) -> bool:
    return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])


class TestRobotInAGrid(unittest.TestCase):
    def test_find_path(self):
        grids = [
            # blocked
            [],
            [[0, 6]],
            [[0, 6], [1, 6], [1, 5], [1, 4], [2, 4]],
            [[3, 6], [2, 5]]
        ]
        for blockedvals in grids:
            grid = [[True for j in range(7)] for i in range(5)]
            for i, j in blockedvals:
                grid[i][j] = False
            print(find_path_memo(grid))

        grid = [[False for j in range(7)] for i in range(5)]
        grid[0][0] = True
        grid[4][6] = True
        print(find_path_memo(grid))


if __name__ == "__main__":
    unittest.main()
