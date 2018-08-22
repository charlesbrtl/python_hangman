class Word(object):

    def __init__(self, hangman_word):
        super(Word, self).__init__()
        self.length = len(hangman_word)
        self.characters = dict()
        for i in range(self.length):

            if self.characters.get(hangman_word[i]) is None:
                self.characters[hangman_word[i]] = []
                self.characters[hangman_word[i]].append(i)
            else:
                self.characters[hangman_word[i]].append(i)
        print(self.characters)


myword = Word("abracadabra")
