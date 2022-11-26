#! /usr/bin/env python3

# -*- coding: utf-8 -*-

import gettext
import random


def guessing_number_game():
    gettext.install(domain='messages', localedir='locales', codeset='utf-8')

    print(_("Welcome player!"))

    # Get username
    player_username = input(_("Enter your username for the game: "))

    # Game info
    print(_("%s, you have to guess a number between 0 and 100") % player_username)

    # Get attempts
    num_of_attempts = get_attempts(player_username)

    # Generate Random Number
    number_to_guess = random.randint(1, 100)

    # Start Game
    attempt = 1  # First attempt
    while attempt <= num_of_attempts:
        guess = ask_guess(attempt)

        # Clues or win
        if guess == number_to_guess:
            print(_("Congratulations %s! You got the number right!") % player_username)
            break
        elif guess > number_to_guess:
            print(_("The number is smaller than %d") % guess)
        else:
            print(_("The number is greater than %d") % guess)

        attempt += 1  # Increase attempt

    if attempt - 1 == num_of_attempts:
        print(_("Wow... looks like you've run out of tries. the number was %d") % number_to_guess)


def ask_guess(attempt):
    guess = 0
    # Duplicated code just for prettier output
    try:
        guess = int(input(_("Attempt %d, what do you think the number is? ") % attempt))
        # In the development there has been an error here but I have not been able to replicate it,
        # even so it has only happened in 1 execution of the multiple ones that have been carried out...
    except ValueError:
        print(_("We want honest players... and who don't play the fool so much!"))
        exit(-1)  # Just to end in this case
    return guess


def get_attempts(player_username):
    num_of_attempts = 0
    while num_of_attempts < 1:
        try:
            num_of_attempts = int(input(_("How many attempts do you want to do? ")))
        except ValueError:
            print(_("We want honest players... and who don't play the fool so much!"))
            exit(-1)  # Just to end in this case

        if num_of_attempts == 0:
            print(_("At least try once %s!") % player_username)
        if num_of_attempts < 0:
            print(_("I don't think negative attempts can be made..."))
    return num_of_attempts


if __name__ == '__main__':
    guessing_number_game()
