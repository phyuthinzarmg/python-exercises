from sys import argv
2
3 script, filename = argv
4
5 txt = open(filename)
6
7 print(f"Here's your file {filename}:")
8 print(txt.read())
9
10 print("Type the filename again:")
11 file_again = input("> ")
12
13 txt_again = open(file_again)
14
15 print(txt_again.read())
