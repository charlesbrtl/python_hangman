class Word(object):

    def __init__(self, hangman_word):
        super(Word, self).__init__()
        self.length = len(hangman_word)
        self.characters = dict()
        self.number_of_guessed_letters = 0
        self.guess = ['_']*int(self.length)

        for i in range(self.length):

            if self.characters.get(hangman_word[i]) is None:
                self.characters[hangman_word[i]] = []
                self.characters[hangman_word[i]].append(i)
            else:
                self.characters[hangman_word[i]].append(i)

        if self.has_letter(' '):
            self.update_guess(' ')

    def has_letter(self, letter):
        return self.characters.get(letter) is not None

    def update_guess(self, letter):
        try:

            for i in self.characters[letter]:
                self.guess[i] = letter

            self.number_of_guessed_letters += int(len(self.characters[letter]))
        except KeyError:
            print("unexpected error")

    def is_guessed(self):
        return self.length == self.number_of_guessed_letters
