class Anagram:
    def __init__(self, word):
        # store the word in lower case
        self.word = word.lower()
        # sort the lower case word
        self.sorted_word = sorted(self.word)

    def match(self, candidates):
        # initialize an empy list to store all the confirmed anagrams
        matches = []
        for candidate in candidates:
            # take each candidate check against the original word and compare against the original word's sorted letters
            if candidate.lower() != self.word and sorted(candidate.lower()) == self.sorted_word:
                matches.append(candidate)
        return matches
