#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import operator
import os

# Start Functions

def clear():
    '''
    Clear console
    '''
    os.system('cls' if os.name=='nt' else 'clear')


def print_words(pos=False):
    '''
    Print words resolves
    Arguments:
    pos - View numbers
    '''
    print_pos = ' '
    print_pos_bar = ' '
    print_pos_letters = ' '
    for i in range(num_letters):
        if pos:
            print_pos = print_pos + str(i + 1) + ' '
            print_pos_bar = print_pos_bar + '| '
        print_pos_letters = print_pos_letters + word_resolve[i] + ' '
    print(print_pos)
    print(print_pos_bar)
    print(print_pos_letters)
    print('')
    print('')

def best_letter(word_resolve):
    '''
    Search best letter
    Arguments:
    word_resolve - list with word resolve
    '''
    # Read all words and count letters
    letters = dict()
    ignore = ('\xb1', '\xc3', '\xb6', '.', '\xae')
    words = open('words.txt')
    # Read alls words for dictionary
    for word in words.readlines():
        # Just consider which have the same length
        if len(word_resolve) == len(word.strip()):
            l_word = list(word.strip().lower())
            # Check word_resolve is same letters
            fit = True
            for i in range(len(l_word)):
                if word_resolve[i] != l_word[i] and word_resolve[i] != '_':
                    fit = False
            # Count the letters
            if fit:
                for letter in l_word:
                    if letter.lower() not in ignore:
                        if letter in letters:
                            letters[letter] = letters[letter] + 1
                        elif not letter in letters_used:
                            letters[letter] = 1
    # Sort
    sorted_letters = sorted(
        letters.items(), key=operator.itemgetter(1), reverse=True
        )
    # Best letter 
    if len(sorted_letters) > 0:
        return sorted_letters[0][0]
    else:
        end = True
        print('No more possibilities')
        return None

# End Functions

# Start 
clear()
print('Hangman Bot 1.0v')
print(' _________     ')
print('|         |    ')
print('|         0    ')
print('|        /|\\  ')
print('|        / \\  ')
print('|              ')
print('|              ')

#  Get num letters and make list resolve
num_letters = input('Number of letters: ')
clear()
play = True
word_resolve = list()
letters_used = list()
for pos in range(num_letters):
    word_resolve.append('_')

print('')
print('Okay, come on!')
print('')

# Logic
while play:
    # Get best letter
    best_option = best_letter(word_resolve)
    if best_option:
        # The guard not to give it back
        letters_used.append(best_option)
        print_words()
        # Print best letter
        print('Test with the letter> {letter}'.format(
            letter=best_option.upper()
            ))
        # Save successes
        print('')
        question_success = raw_input('I successful? (yes o no): ').lower()
        clear()
        if question_success == 'no':
            clear()
            print('')
            print('Ups!')
        elif question_success == 'yes':
            print('')
            print_words(True)
            good_pos = raw_input('Tell me that positions (Example> 2 4 7): ').split(' ')
            clear()
            for pos in good_pos:
                word_resolve[int(pos) - 1] = best_option

    # Game over
        end = False
        if not '_' in word_resolve:
            end = True
    if end:
        play = False
        print('Game over :)')