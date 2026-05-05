# Write a function that takes two strings and checks whether they are anagrams of each other.

from collections import Counter

def if_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        return Counter(word1.lower()) == Counter(word2.lower())
print(if_anagram("Care","Race"))