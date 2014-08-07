import sys
# Part 1: store all words from unix default dictionary into a python dictionary.
# The keys are sorted word and values are all valid words of the sorted string.
# For example values stored in key 'dgo' are ['dog', 'god', 'god']

sorted_dict = {}
with open("/usr/share/dict/words", "r") as f:
    for word in f:
        word = word.strip().lower()
        sorted_word = ''.join(sorted(word))
        sorted_dict.setdefault(sorted_word,[]).append(word)

#Part 2: Recursively compute all possible strings

def permute(inputstr):
    for i in range(len(inputstr)):
        yield(inputstr[i])        
        for s in permute(inputstr[:i] + inputstr[i+1:]):
            yield(inputstr[i] + s)

#Part 3: Sift through the elements and find out if they are part of dictionary.
# Do this by sorting each word and comparing it against the already sorted dictionary key
def jumble(word):	    
    for elem in permute(word)	    :
        sorted_elem = ''.join(sorted(elem))
        if sorted_elem in sorted_dict:
            if elem in sorted_dict[sorted_elem]:
                print elem

word=raw_input('Enter a word: ')
jumble(word)
