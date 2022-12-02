''' 
Template file
'''

import time

FILE_NAME = '02/input.txt'



def main():
    # Process the input file
    with open(FILE_NAME, 'r') as inputfile:
        input_lines = inputfile.read().splitlines()

    '''
    PART ONE
    '''
    
    scores_partone = {
         'A X':4 # 1 for rock, 3 for draw
        ,'A Y':8 # 2 for paper, 6 for win
        ,'A Z':3 # 3 for scissors, 0 for loss
        ,'B X':1 # 1 for rock, 0 for loss
        ,'B Y':5 # 2 for paper, 3 for draw
        ,'B Z':9 # 3 for scissors, 6 for win
        ,'C X':7 # 1 for rock, 6 for win
        ,'C Y':2 # 2 for paper, 0 for loss
        ,'C Z':6 # 3 for scissors, 3 for draw
    }
    total_score = 0
    for line in input_lines:
        total_score += scores_partone[line]
    print(f'Part one answer: {total_score}')

    '''
    PART TWO
    '''
    
    scores_parttwo = {
         'A X':3 # 0 for loss, 3 for scissors
        ,'A Y':4 # 3 for draw, 1 for rock
        ,'A Z':8 # 6 for win, 2 for paper
        ,'B X':1 # 0 for loss, 1 for rock
        ,'B Y':5 # 3 for draw, 2 for paper
        ,'B Z':9 # 6 for win, 3 for scissors
        ,'C X':2 # 0 for loss, 2 for paper
        ,'C Y':6 # 3 for draw, 3 for scissors
        ,'C Z':7 # 6 for win, 1 for rock
    }
    total_score = 0
    for line in input_lines:
        total_score += scores_parttwo[line]
    print(f'Part two answer: {total_score}')

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'All done! Total time was {(end_time - start_time):.3f} seconds.')
