# your code goes here!
class Anagram:
    
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])
        
    def match(self, words):
        anagram_test = []
        
        for word in words:
            if sorted([letter for letter in word]) == self.word_letters:
                anagram_test.append(word)
        
        return anagram_test
        