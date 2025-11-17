__author__ = "Fabian Ha"

import sys
import heapq


def load_maze(s):
    maze = {}
    with open(s, "r") as f:
        for i, line in enumerate(f):
            for j in range(len(line)):
                maze[(i, j)] = line[j]
    return maze

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

next_positions = [(0, 0)]

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(maze, start, goal: tuple):
    g_score = {(cell[0], cell[1]):float("inf") for cell in maze.keys()}
    g_score[start] = 0
    f_score = {(cell[0], cell[1]):float("inf") for cell in maze.keys()}
    f_score[start] = h(start, goal)

    open = [(h(start, goal), h(start, goal), start)]
    aPath = {}

    while len(open) > 0:
        currCell = heapq.heappop(open)[2]
        if currCell == goal:
            break

        for direction in directions:
            new_y = currCell[0] + direction[0]
            new_x = currCell[1] + direction[1]
            newCell = (new_y, new_x)

            if newCell in maze and maze[newCell] != "#":
                temp_g_score = g_score[currCell]
                temp_f_score = temp_g_score + h(newCell, goal)

                if temp_f_score < f_score[newCell]:
                    g_score[newCell] = temp_g_score
                    f_score[newCell] = temp_f_score
                    open.append((temp_f_score, h(newCell, goal), newCell))
                    aPath[newCell] = currCell

    forwardPath = []
    cell = goal
    while cell != start:
        forwardPath.append(cell)
        cell = aPath[cell]

    forwardPath.append(cell)

    return forwardPath

from timer import time_function

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    goal = (1, 1)

    maze1 = load_maze("l1.txt")
    print("Labyrinth 1")
    print(a_star(maze1, (11, 6), goal))

    time_function(a_star(maze1, (11, 6), goal), False)

    print("\nLabyrinth 2")
    maze2 = load_maze("l2.txt")
    time_function(a_star(maze2, (30, 29), goal), False)

    print("\nLabyrinth 3")
    maze3 = load_maze("l3.txt")
    time_function(a_star(maze3, (200, 199), goal), False)

    print("\nLabyrinth 4")
    maze4 = load_maze("l4.txt")
    time_function(a_star(maze4, (200, 298), goal), False)

    print("\nLabyrinth 5")
    maze5 = load_maze("l5.txt")
    time_function(a_star(maze5, (200, 1), goal), False)

    print("\nLabyrinth 6")
    maze6 = load_maze("l6.txt")
    time_function(a_star(maze6, (0, 280), goal), False)
