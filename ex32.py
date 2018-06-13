for number in the_count:
7 print(f"This is count {number}")
8
9 # same as above
10 for fruit in fruits:
11 print(f"A fruit of type: {fruit}")
12
13 # also we can go through mixed lists too
14 # notice we have to use {} since we don't know what's in it
15 for i in change:
16 print(f"I got {i}")
17
18 # we can also build lists, first start with an empty one
19 elements = []
20
21 # then use the range function to do 0 to 5 counts
22 for i in range(0, 6):
23 print(f"Adding {i} to the list.")
24 # append is a function that lists understand
25 elements.append(i)
26
27 # now we can print them out too
28 for i in elements:
29 print(f"Element was: {i}")the_count = [1, 2, 3, 4, 5]
2 fruits = ['apples', 'oranges', 'pears', 'apricots']
3 change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
4
5 # this first kind of for-loop goes through a list
