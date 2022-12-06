import time

FILE_NAME = '04/input.txt'

def main():
    # Process the input file
    with open(FILE_NAME, 'r') as inputfile:
        input_lines = inputfile.read().splitlines()

    '''
    PART ONE

    Consider each pair of number ranges. Find the count of number range pairs
    in which one fully contains the other.
    '''

    intersection_count = 0

    for line in input_lines:
        left_positions = line.split(',')[0].split('-')
        right_positions = line.split(',')[1].split('-')
        
        left_set = set(range(int(left_positions[0]), int(left_positions[1]) + 1))
        right_set = set(range(int(right_positions[0]), int(right_positions[1]) + 1))

        if left_set.intersection(right_set) == left_set or left_set.intersection(right_set) == right_set:
            intersection_count += 1

    print(f'Part one answer: {intersection_count}')
 
    '''
    PART TWO

    Consider each pair of number ranges. Find the count of number range pairs
    in which one overlaps the other at all.
    '''

    overlap_count = 0

    for line in input_lines:
        left_positions = line.split(',')[0].split('-')
        right_positions = line.split(',')[1].split('-')

        if ((
                int(left_positions[1]) >= int(right_positions[0])
                and 
                int(left_positions[1]) <= int(right_positions[1])
            ) or (
                int(right_positions[1]) >= int(left_positions[0])
                and
                int(right_positions[1]) <= int(left_positions[1])
            )):
            overlap_count += 1

    print(f'Part two answer: {overlap_count}')

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'All done! Total time was {(end_time - start_time):.3f} seconds.')
