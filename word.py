class Word(object):

    def __init__(self, hangman_word):
        super(Word, self).__init__()
        self.length = len(hangman_word)
        self.characters = dict()
        self.guessed_letters = 0
        self.guess = ['_']*int(self.length)
        for i in range(self.length):

            if self.characters.get(hangman_word[i]) is None:
                self.characters[hangman_word[i]] = []
                self.characters[hangman_word[i]].append(i)
            else:
                self.characters[hangman_word[i]].append(i)

    def get_guess(self):
        return self.guess

    def has_letter(self, letter):
        return self.characters.get(letter) is not None

    def update_guess(self, letter):
        try:
            self.guessed_letters += int(len(self.characters[letter]))
            for i in self.characters[letter]:
                self.guess[i] = letter
        except KeyError:
            print("unexpected error")



other = Word("unitedkingdom")
print(other.has_letter('z'))
other.update_guess('k')
print(other.get_guess())
print(other.guessed_letters)