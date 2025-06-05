import random
import os
import time

WIDTH = 40
HEIGHT = 20

# random seed of living cells
cells = set()
for y in range(HEIGHT):
    for x in range(WIDTH):
        if random.random() < 0.3:
            cells.add((x, y))


def neighbors(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx or dy:
                yield ((x + dx) % WIDTH, (y + dy) % HEIGHT)


def step(cells):
    new_cells = set()
    counts = {}
    for x, y in cells:
        for nx, ny in neighbors(x, y):
            counts[(nx, ny)] = counts.get((nx, ny), 0) + 1
    for pos, count in counts.items():
        if count == 3 or (count == 2 and pos in cells):
            new_cells.add(pos)
    return new_cells


while True:
    os.system('clear')
    for y in range(HEIGHT):
        line = ''
        for x in range(WIDTH):
            line += '*' if (x, y) in cells else ' '
        print(line)
    cells = step(cells)
    time.sleep(0.1)
