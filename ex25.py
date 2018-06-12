def break_words(stuff):
2 """This function will break up words for us."""
3 words = stuff.split(' ')
4 return words
5
6 def sort_words(words):
7 """Sorts the words."""
8 return sorted(words)
9
10 def print_first_word(words):
11 """Prints the first word after popping it off."""
12 word = words.pop(0)
13 print(word)
14
15 def print_last_word(words):
16 """Prints the last word after popping it off."""
17 word = words.pop(-1)
18 print(word)
19
20 def sort_sentence(sentence):
21 """Takes in a full sentence and returns the sorted words."""
22 words = break_words(sentence)
23 return sort_words(words)
24
25 def print_first_and_last(sentence):
26 """Prints the first and last words of the sentence."""
27 words = break_words(sentence)
28 print_first_word(words)
29 print_last_word(words)
30
31 def print_first_and_last_sorted(sentence):
32 """Sorts the words then prints the first and last one."""
words = sort_sentence(sentence)
34 print_first_word(words)
35 print_last_word(words)
