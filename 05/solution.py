import collections as col
import copy
import time

FILE_NAME = '05/input.txt'

def process_input():
    # Process the input file
    with open(FILE_NAME, 'r') as inputfile:
        input_lines = inputfile.read().splitlines()

    # process the input file
    stacks = []
    moves = []
    mode = 0
    
    for line in input_lines:
        if line == '' or line[1] == '1':
            mode = 1
        elif mode == 0:
            # define the stack array
            if not stacks:
                stack_count = int((len(line) + 1) / 4)
                stacks = [col.deque() for i in range(stack_count)]

            # process each line
            for i in range(stack_count):
                index = (i * 4) + 1
                if line[index] != ' ':
                    stacks[i].append(line[index])
        elif mode == 1:
            # process the move list
            components = line.split(' ')
            piece_count = int(components[1])
            from_index = int(components[3])
            to_index = int(components[5])
            moves.append((piece_count, from_index, to_index))

    return stack_count, stacks, moves

def main():
    stack_count, stacks, moves = process_input()   

    '''
    PART ONE
    '''

    # execute the moves
    part_one_stacks = copy.deepcopy(stacks)
    for instruction in moves:
        from_index = instruction[1] - 1
        to_index = instruction[2] - 1
        for i in range(instruction[0]):
            cargo = part_one_stacks[from_index].popleft()
            part_one_stacks[to_index].appendleft(cargo)

    # get output string
    top_crates = ''
    for i in range(stack_count):
        top_crates += part_one_stacks[i][0]

    print(f'Part one answer: {top_crates}')

    '''
    PART TWO
    '''

    # execute moves with new logic
    part_two_stacks = copy.deepcopy(stacks)
    for instruction in moves:
        cargo = col.deque()
        from_index = instruction[1] - 1
        to_index = instruction[2] - 1
        for i in range(instruction[0]):
            cargo.append(part_two_stacks[from_index].popleft())
        part_two_stacks[to_index] = cargo + part_two_stacks[to_index]

    # get output string
    top_crates = ''
    for i in range(stack_count):
        top_crates += part_two_stacks[i][0]

    print(f'Part two answer: {top_crates}')

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'All done! Total time was {(end_time - start_time):.3f} seconds.')
