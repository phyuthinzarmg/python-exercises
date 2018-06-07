from sys import argv
2
3 script, user_name = argv
4 prompt = '> '
5
6 print(f"Hi {user_name}, I'm the {script} script.")
7 print("I'd like to ask you a few questions.")
8 print(f"Do you like me {user_name}?")
9 likes = input(prompt)
10
11 print(f"Where do you live {user_name}?")
12 lives = input(prompt)
13
14 print("What kind of computer do you have?")
15 computer = input(prompt)
16
17 print(f"""
18 Alright, so you said {likes} about liking me.
19 You live in {lives}. Not sure where that is.
20 And you have a {computer} computer. Nice.
21 """)
