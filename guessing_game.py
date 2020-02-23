#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guessing a number in a user defined range. 
Run the script: python3 guessing_game.py number1 number2

@author: hannahannuniemi
"""

from random import randint
import sys


def run_guess(guess, answer):
    if  0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False

if __name__ == '__main__':
    answer = randint(int(sys.argv[1]), int(sys.argv[2]))
    while True:
        try:
            guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue