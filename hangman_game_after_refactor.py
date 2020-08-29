import random

# get a random word for user to guess


def get_config():
    return {
        "init_life": 6
    }


def get_word_list():
    return [
        "tiger",
        "police",
        "woman",
        "inline"
    ]


def get_random_word(word_list):
    return random.choice(word_list)


# gen title line to ask user to guess the secret word
def get_title_lines(num_of_chances, secret_word):
    return """
    HANGMAN

    Guess the secret word! You only have {} chances!
    Secret-word have {} letters.
    """.format(num_of_chances, len(secret_word))


# get number of wrong guesses by secret word and user guesses
def get_number_of_wrong_guesses(s_word, guess_list):
    count = 0
    for i in guess_list:
        if i not in s_word:
            count += 1
    return count

# One letter guesses


def check_cond1(guessed):
    if len(guessed) == 1:
        return "", True
    return "Only a single letter is allowed", False

# No repetitive guesses


def check_cond2(guessed, guess_list):
    if not guessed in guess_list:
        return "", True
    return "Already guessed '{}'".format(guessed), False

# Only alphabets


def check_cond3(guessed):
    if guessed.isalpha():
        return "", True
    return "Only alphabets are allowed", False


def upper_to_lower(guess):
    if guess.isupper():
        return guess.lower()
    return guess

# guess_evaluator: checks all the input-conditions


def guess_evaluator(guessed, guess_list):
    guessed = upper_to_lower(guessed)
    if not check_cond1(guessed)[1]:
        return check_cond1(guessed)
    if not check_cond2(guessed, guess_list)[1]:
        return check_cond2(guessed, guess_list)
    if not check_cond3(guessed)[1]:
        return check_cond3(guessed)

    return "", True

# masks letters in 's_word' unless they are in 'guessed'


def mask_word(s_word, guessed):
    mask = []
    for i in s_word:
        if i in guessed:
            mask.append(i)
        else:
            mask.append("*")
    return "".join(mask)


# ask user to input again when input leter is invalid
def guess_manager(guessed, guess_list):
    while not guess_evaluator(guessed, guess_list)[1]:
        print(guess_evaluator(guessed, guess_list)[0])
        guessed = input("Enter another guess: ")
    return guessed


# the game process
def game_process(secret_word, init_life):
    formatter = "\nWord: {:^15}    Life:{:<12}   Guessed: {:<10}"
    guesslist = ""
    game_won = False

    while not get_number_of_wrong_guesses(secret_word, guesslist) == init_life:
        newguess = input("Enter a guess: ")
        # if the guess letter is invalid, ask to input again.
        newguess = guess_manager(newguess, guesslist)

        guesslist += newguess
        guesslist = "".join(sorted(set(guesslist)))

        life = " {} left".format(
            init_life - get_number_of_wrong_guesses(secret_word, guesslist))
        print(formatter.format(mask_word(secret_word, guesslist), life, guesslist))

        if secret_word == mask_word(secret_word, guesslist):
            return "\n\nCongratulations!"

    if not game_won:
        return "\nToo bad! The secret word was '{}'".format(secret_word)


def main():
    config = get_config()
    init_life = config["init_life"]
    word_list = get_word_list()
    secret_word = get_random_word(word_list)
    title_lines = get_title_lines(init_life, secret_word)

    print(title_lines)

    result = game_process(secret_word, init_life)

    print(result)


if __name__ == '__main__':
    main()
