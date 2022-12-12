import time

FILE_NAME = '06/input.txt'

def process_input():
    # Process the input file
    with open(FILE_NAME, 'r') as inputfile:
        input_lines = inputfile.read()
        return input_lines


def find_start_marker(string, number_of_characters):
    for i in range(number_of_characters, len(string)):
        subset = string[i - number_of_characters:i]
        unique_chars = ''
        for char in subset:
            if unique_chars.find(char) == -1:
                unique_chars += char
        if len(unique_chars) == number_of_characters:
            return i 


def main():
    input_str = process_input()

    '''
    PART ONE
    '''
    answer = find_start_marker(input_str, 4)
    print(f'Part one answer: {answer}')


    '''
    PART TWO
    '''
    answer = find_start_marker(input_str, 14)
    print(f'Part two answer: {answer}')


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'All done! Total time was {(end_time - start_time):.3f} seconds.')
