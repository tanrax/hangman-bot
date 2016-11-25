#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import operator
import os

words = open('words.txt')
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def best_letter(word_resolve):
    # Read all words and count letters
    letters = dict()
    ignore = ('\xb1', '\xc3', '\xb6', '.', '\xae')
    # Read alls words for dictionary
    for word in words.readlines():
        # Just consider which have the same length
        if len(word_resolve) == len(word):
            l_word = list(word.strip().lower())
            # Count the letters
            for letter in l_word:
                if letter.lower() not in ignore:
                    if letter in letters:
                        letters[letter] = letters[letter] + 1
                    else:
                        letters[letter] = 1
    # Sort
    sorted_letters = sorted(
        letters.items(), key=operator.itemgetter(1), reverse=True
        )

    # Best letter 
    return sorted_letters[0][0]

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
word_resolve = list()
letters_used = list()
for pos in range(num_letters):
    word_resolve.append('_')

print('')
print('Okay, come on!')
print('')
print('')
# Logic
while True:
    # Get best letter
    best_option = best_letter(word_resolve)
    # The guard not to give it back
    letters_used.append(best_option)
    # Print best letter
    print('Test with the letter> {letter}'.format(
        letter=best_option.upper()
        ))
    # Save successes
    print('')
    question_success = raw_input('I successful? (yes o no): ').lower()
    clear()
    if question_success == 'no':
        print('')
        print('Ups!')
        print('')
        print('')
    elif question_success == 'yes':
        print_pos = ' '
        print_pos_bar = ' '
        print_pos_letters = ' '
        for i in range(num_letters):
            print_pos = print_pos + str(i + 1) + ' '
            print_pos_bar = print_pos_bar + '| '
            print_pos_letters = print_pos_letters + word_resolve[i] + ' '
        print(print_pos)
        print(print_pos_bar)
        print(print_pos_letters)
        print('')
        good_pos = raw_input('Tell me that positions (Example> 2 4 7): ')
