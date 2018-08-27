from game_elements.word import Word


class Game(object):
    def __init__(self, word, difficulty):
        super(Game, self).__init__()
        self.word = Word(word)
        self.difficulty = difficulty
        self.lives = 10
