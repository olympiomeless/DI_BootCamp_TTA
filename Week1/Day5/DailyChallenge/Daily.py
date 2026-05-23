#Daily 1
def sort_funct(lst):
    return sorted(lst, key=lambda x: x[1])

words = ("without", "hello", "bag", "world")

print(sort_funct(words))

#Daily 2
def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

print(longest_word("Margaret's toy is a pretty doll."))