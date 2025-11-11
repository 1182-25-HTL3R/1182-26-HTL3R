__author__ = "Fabian Ha"

import sys


def load_maze(s):
    maze = []
    with open(s, "r") as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def tiefensuche(maze, position: tuple, path: list, visited: set = None):
    if visited is None:
        visited = set()
    path.append(position)
    available_ways = []
    for direction in directions:
        new_x = position[0] + direction[0]
        new_y = position[1] + direction[1]

        if maze[new_y][new_x] == 'A':
            path.append((new_x, new_y))
            return path

        if maze[new_y][new_x] == ' ':
            if (new_x, new_y) not in visited:
                available_ways.append((new_x, new_y))

    for way in available_ways:
        visited.add(way)
        if out := tiefensuche(maze, way, path, visited):
            return out

    return None

from timer import time_function

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    start = (1, 1)

    maze1 = load_maze("l1.txt")
    print("Labyrinth 1")
    time_function(tiefensuche(maze1, start, list()), False)

    print("\nLabyrinth 2")
    maze2 = load_maze("l2.txt")
    time_function(tiefensuche(maze2, start, list()), False)

    print("\nLabyrinth 3")
    maze3 = load_maze("l3.txt")
    time_function(tiefensuche(maze3, start, list()), False)

    print("\nLabyrinth 4")
    maze4 = load_maze("l4.txt")
    time_function(tiefensuche(maze4, start, list()), False)

    print("\nLabyrinth 5")
    maze5 = load_maze("l5.txt")
    time_function(tiefensuche(maze5, start, list()), False)

    print("\nLabyrinth 6")
    maze6 = load_maze("l6.txt")
    time_function(tiefensuche(maze6, start, list()), False)
