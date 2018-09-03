import string


class Model(object):
    def __init__(self, difficulty):
        super(Model, self).__init__()
        self.lives = 10
        self.letter_tries = dict.fromkeys(string.ascii_lowercase, False)
        self.difficulty = difficulty

    def check_letter_is_checked(self, letter):
        return self.letter_tries[letter]

    def check_letter(self, letter):
        self.letter_tries[letter] = True

    def return_unchecked(self):
        unchecked = []
        for key, value in self.letter_tries.items():
            if value:
                unchecked.append(key)
        return unchecked

    def lost(self):
        return self.lives == 0

    def lose_life(self):
        self.lives -= 1
