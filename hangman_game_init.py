import random

# get a random word for user to guess


def get_random_word():
    pass

# gen title line to ask user to guess the secret word


def get_title_lines(num_of_chances, secret_word):
    pass

# get number of wrong guesses by secret word and user guesses


def get_number_of_wrong_guesses(s_word, guess_list):
    pass

# One letter guesses


def check_cond1(guessed):
    pass

# No repetitive guesses


def check_cond2(guessed, guess_list):
    pass

# Only alphabets


def check_cond3(guessed):
    pass


def upper_to_lower(guess):
    pass

# guess_evaluator: checks all the input-conditions


def guess_evaluator(guessed, guess_list):
    pass

# masks letters in 's_word' unless they are in 'guessed'


def mask_word(s_word, guessed):
    pass

# ask user to input again when input leter is invalid


def guess_manager(guessed, guess_list):
    pass

# the game process


def game_process(secret_word):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
