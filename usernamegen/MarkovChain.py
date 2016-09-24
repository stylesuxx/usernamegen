import random


class MarkovChain:
    def __init__(self, words, size):
        self.size = size
        self.starts = map(lambda word: word[:self.size], words)
        self.lookup = self._buildLookupTable(words)

    def _buildLookupTable(self, words):
        lookup = {}
        for word in words:
            for key, val in self._tuples(word):
                if key in lookup:
                    lookup[key].append(val)

                else:
                    lookup[key] = [val]

        return lookup

    def _tuples(self, word):
        word = word.strip()
        if len(word) >= self.size:
            word = word + "\n"
            for i in range(len(word) - self.size):
                yield(word[i:i + self.size], word[i + self.size])

    def getWord(self):
        key = random.choice(self.starts)
        word = key
        try:
            next = random.choice(self.lookup[key])
            while next != "\n":
                word = word + next
                key = key[1:] + next
                next = random.choice(self.lookup[key])
        except KeyError:
            pass

        return word
