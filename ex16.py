from sys import argv
2
3 script, filename = argv
4
5 print(f"We're going to erase {filename}.")
6 print("If you don't want that, hit CTRL-C (^C).")
7 print("If you do want that, hit RETURN.")
8
9 input("?")
10
11 print("Opening the file...")
12 target = open(filename, 'w')
13print("Truncating the file. Goodbye!")
15 target.truncate()
16
17 print("Now I'm going to ask you for three lines.")
18
19 line1 = input("line 1: ")
20 line2 = input("line 2: ")
21 line3 = input("line 3: ")
22
23 print("I'm going to write these to the file.")
24
25 target.write(line1)
26 target.write("\n")
27 target.write(line2)
28 target.write("\n")
29 target.write(line3)
30 target.write("\n")
31
32 print("And finally, we close it.")
33 target.close()
