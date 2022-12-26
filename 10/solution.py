import numpy as np
import time

FILE_NAME = '10/input.txt'

def process_input():
    with open(FILE_NAME, 'r') as inputfile:
        input_lines = inputfile.read().splitlines()
        
    output_array = np.array([1])
    for line in input_lines:
        output_array = np.append(output_array, 0) 
        if line != 'noop':
            output_array = np.append(output_array, int(line[5:]))

    return output_array

def main():
    register_shifts = process_input()
    
    '''
    PART ONE
    '''
    
    register_value = 0
    values = []

    for i, value in enumerate(register_shifts):
        if i in (20, 60, 100, 140, 180, 220):
            values.append(register_value * i)
        
        register_value += value
    
    print(f'Part one answer: {sum(values)}')

    '''
    PART TWO
    '''

    register_value = 0

    for i, value in enumerate(register_shifts):
        if i == 0:
            output_str = ''
            register_value += value

        else:
            pixel_pos = (i % 40) - 1

            if abs(register_value - pixel_pos) < 2:
                output_str += '#'
            else:
                output_str += '.'

            register_value += value

            if i % 40 == 0:
                print(output_str)
                output_str = ''

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'All done! Total time was {(end_time - start_time):.3f} seconds.')
