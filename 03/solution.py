import time

FILE_NAME = '03/input.txt'

def main():
    # Process the input file
    with open(FILE_NAME, 'r') as inputfile:
        input_lines = inputfile.read().splitlines()

    
    priorities = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    '''
    PART ONE
    
    Split each input line in half and find the common character. Then sum the "score"
    of each common character.
    '''

    char_score = 0

    for line in input_lines:
        split_pos = int(len(line) / 2)
        left_str = line[:split_pos]
        right_str = line[split_pos:]
        common_chars = set(left_str).intersection(right_str)
        char_score += priorities.find(common_chars.pop())

    print(f'Part one answer: {char_score}')

    '''
    PART TWO

    Consider sets of three input lines. Find the common character between all three.
    Then sum the "score" of each common character.
    '''

    badge_score = 0

    for i in range(0, int(len(input_lines) / 3)):
        line1 = input_lines[(i * 3)]
        line2 = input_lines[(i * 3) + 1]
        line3 = input_lines[(i * 3) + 2]
        common_chars = set(line1).intersection(line2).intersection(line3)
        badge_score += priorities.find(common_chars.pop())

    print(f'Part two answer: {badge_score}')

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'All done! Total time was {(end_time - start_time):.3f} seconds.')
