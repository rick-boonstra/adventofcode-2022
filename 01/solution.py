import time

FILE_NAME = '01/input.txt'

def main():
    # Process the input file
    with open(FILE_NAME, 'r') as inputfile:
        input_lines = inputfile.read().splitlines()

    '''
    PART ONE
    Iterate over a list of individual rations carriend by each elf
    and return the highest total found.
    '''

    calories_per_elf = []

    for line in input_lines:
        if calories_per_elf == [] or line == '':
            calories_per_elf.append(0)
        else:
            calories_per_elf[-1] += int(line)

    max_calories = max(calories_per_elf)
    print(f'Part one answer: {max_calories}')

    '''
    PART TWO
    Iterate over a list of individual rations carriend by each elf
    and return the sum of the three highest totals found.
    '''

    top_three = sorted(calories_per_elf, reverse = True)[:3]
    print(f'Part two answer: {sum(top_three)}')

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'All done! Total time was {(end_time - start_time):.3f} seconds.')
