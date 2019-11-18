import numpy as np

class cell(self):
    def __init__(self):
        self.state = 0

    def toggle_state (self):
        self.state = not(self.state)

def generate_array(row, col):
    grid = np.zeros((row, col))
    return grid

def check_valid(grid,index):

    max_x = len(grid,0)
    max_y = len(grid,1)
    min = 0

    if index(0) > max_x or index(1) > max_y or index(0) < min or index(1) < min:
        result = False
    else
        result = True

    return result

def neighbors(grid, index):

    min_x = index(0) - 1
    max_x = index(0) + 1
    min_y = index(1) - 1
    min_y = index(1) + 1

    count = -1
    for i in range(min_x,max_x):
        for j in range(min_y,max_y):
            if check_valid(i,j):
                count += 1

    return num_neighbors