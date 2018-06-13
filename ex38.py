ten_things = "Apples Oranges Crows Telephone Light Sugar"
2
3 print("Wait there are not 10 things in that list. Let's fix that.")
4
5 stuff = ten_things.split(' ')
6 more_stuff = ["Day", "Night", "Song", "Frisbee",
7 "Corn", "Banana", "Girl", "Boy"]
8
9 while len(stuff) != 10:
10 next_one = more_stuff.pop()
11 print("Adding: ", next_one)
12 stuff.append(next_one)
13 print(f"There are {len(stuff)} items now.")
14
15 print("There we go: ", stuff)
16
17 print("Let's do some things with stuff.")
18
19 print(stuff[1])
20 print(stuff[-1]) # whoa! fancy
21 print(stuff.pop())
22 print(' '.join(stuff)) # what? cool!
23 print('#'.join(stuff[3:5])) # super stellar!
