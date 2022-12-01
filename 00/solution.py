''' 
Template file
'''

import time

FILE_NAME = '01/test-input.txt'

def main():
    # Process the input file
    with open(FILE_NAME, 'r') as inputfile:
        input_lines = inputfile.read().splitlines()
        cleaned_list = [int(x) for x in input_lines]

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'All done! Total time was {(end_time - start_time):.3f} seconds.')
