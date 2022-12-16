import numpy as np
import time

FILE_NAME = '08/input.txt'

def process_input():
    # Process the input file
    with open(FILE_NAME, 'r') as inputfile:
        input_lines = inputfile.read().splitlines()
        row_count = len(input_lines)
        col_count = len(input_lines[0])    
        tree_grid = np.zeros(shape=(row_count, col_count))

        for index, line in enumerate(input_lines):
            tree_grid[index] = [int(x) for x in line]
    
    return tree_grid, row_count, col_count

def is_visible(tree_grid, x_pos, y_pos):
    up = tree_grid[:,x_pos][0:y_pos]
    down = tree_grid[:,x_pos][y_pos + 1:]
    left = tree_grid[y_pos,:][0:x_pos]
    right = tree_grid[y_pos,:][x_pos + 1:]
    
    if (
        max(up) < int(tree_grid[y_pos][x_pos])
        or max(down) < int(tree_grid[y_pos][x_pos])
        or max(left) < int(tree_grid[y_pos][x_pos])
        or max(right) < int(tree_grid[y_pos][x_pos])
    ):
        return 1
    else:
        return 0

def tree_score(tree_grid, x_pos, y_pos):
    up = np.flip(tree_grid[:,x_pos][0:y_pos])
    down = tree_grid[:,x_pos][y_pos + 1:]     
    left = np.flip(tree_grid[y_pos,:][0:x_pos])
    right = tree_grid[y_pos,:][x_pos + 1:]
    tree_height = tree_grid[y_pos][x_pos]

    up_score = 0
    for i in range(0, len(up)):
        if up[i] <= tree_height:
            up_score += 1
        if up[i] >= tree_height:
            break

    down_score = 0
    for i in range(0, len(down)):
        if down[i] <= tree_height:
            down_score += 1
        if down[i] >= tree_height:
            break

    left_score = 0
    for i in range(0, len(left)):
        if left[i] <= tree_height:
            left_score += 1
        if left[i] >= tree_height:
            break

    right_score = 0
    for i in range(0, len(right)):
        right_score += 1
        if right[i] >= tree_height:
            break

    return up_score * down_score * left_score * right_score

def main():
    tree_grid, row_count, col_count = process_input()
    
    '''
    PART ONE
    '''
    visible_trees = (row_count + col_count - 2) * 2 # all outside trees are visible
    for i in range(1, row_count - 1): # ignore outermost rows
        for j in range(1, col_count - 1): #ignore outermost columns
            visible_trees += is_visible(tree_grid, j, i)

    print(f'Part one answer: {visible_trees}')

    '''
    PART TWO
    '''
    max_score = 0
    for i in range(1, row_count - 1): # ignore outermost rows
        for j in range(1, col_count - 1): #ignore outermost columns
            score = tree_score(tree_grid, j, i)
            if score > max_score:
                max_score = score
    print(f'Part two answer: {max_score}')

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'All done! Total time was {(end_time - start_time):.3f} seconds.')
