import unittest
import hangman_game


class TestStringMethods(unittest.TestCase):

    # test get random word can return a proper word
    def test_get_random_word(self):
        self.assertGreater(len(hangman_game.get_random_word(["tiger", "police", "something"])), 0)

    def test_get_title_lines(self):
        self.assertEqual(hangman_game.get_title_lines(6, "abcdef"), """
    HANGMAN

    Guess the secret word! You only have 6 chances!
    Secret-word have 6 letters.
    """)

    def test_wrong_guesses(self):
        words = ["python", "tigers", "whales", "elephant"]
        guesslist = ["lthwea", "qwerty", "asdfe", "qwdtfe"]
        result = [4, 3, 2, 4]
        for i in range(len(words)):
            self.assertEqual(hangman_game.get_number_of_wrong_guesses(
                words[i], guesslist[i]), result[i])

    def test_check_cond1(self):
        guess = ["you", "we", "u", "i", "v"]
        result = [("Only a single letter is allowed", False),
                  ("Only a single letter is allowed", False), ("", True), ("", True), ("", True)]
        for i in range(len(guess)):
            self.assertEqual(hangman_game.check_cond1(guess[i]), result[i])

    def test_check_cond2(self):
        guess_f = ["a", "b", "c"]
        guess_t = ["d", "e", "f"]
        guess_list = "qawbrc"
        for i in range(len(guess_t)):
            self.assertEqual(hangman_game.check_cond2(
                guess_t[i], guess_list), ("", True))
        for i in range(len(guess_f)):
            self.assertEqual(hangman_game.check_cond2(
                guess_f[i], guess_list), (
                "Already guessed '{}'".format(guess_f[i]), False))

    def test_check_cond3(self):
        guess = ["1", "?", "n", "o", "f"]
        result = [("Only alphabets are allowed", False),
                  ("Only alphabets are allowed", False), ("", True), ("", True), ("", True)]
        for i in range(len(guess)):
            self.assertEqual(hangman_game.check_cond3(guess[i]), result[i])

    def test_upper_to_lower(self):
        guess = ["A", "B", "C", "d", "e", "f"]
        result = ["a", "b", "c", "d", "e", "f"]
        for i in range(len(guess)):
            self.assertEqual(hangman_game.upper_to_lower(guess[i]), result[i])

    def test_guess_evaluator(self):
        guess = ["A", "e", "f"]
        guess_list = "zxy"
        result = [("", True), ("", True), ("", True)]
        for i in range(len(guess)):
            self.assertEqual(hangman_game.guess_evaluator(
                guess[i], guess_list), result[i])

    def test_guess_evaluator_cond1(self):
        guess = ["wou", "sss", "123", "zy"]
        guess_list = "zxy"
        result = ("Only a single letter is allowed", False)
        for i in range(len(guess)):
            self.assertEqual(hangman_game.guess_evaluator(
                guess[i], guess_list), result)

    def test_guess_evaluator_cond2(self):
        guess = ["x", "z", "y"]
        guess_list = "xzy"
        for i in range(len(guess)):
            self.assertEqual(hangman_game.guess_evaluator(guess[i], guess_list), (
                "Already guessed '{}'".format(guess[i]), False))

    def test_guess_evaluator_cond3(self):
        guess = ["?", "1", "#"]
        guess_list = "zxy"
        result = ("Only alphabets are allowed", False)
        for i in range(len(guess)):
            self.assertEqual(hangman_game.guess_evaluator(
                guess[i], guess_list), result)


if __name__ == '__main__':
    unittest.main()
