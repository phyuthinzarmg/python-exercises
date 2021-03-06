
# create a mapping of state to abbreviation
2 states = {
3 'Oregon': 'OR',
4 'Florida': 'FL',
5 'California': 'CA',
6 'New York': 'NY',
7 'Michigan': 'MI'
8 }
9
10 # create a basic set of states and some cities in them
cities = {
12 'CA': 'San Francisco',
13 'MI': 'Detroit',
14 'FL': 'Jacksonville'
15 }
16
17 # add some more cities
18 cities['NY'] = 'New York'
19 cities['OR'] = 'Portland'
20
21 # print out some cities
22 print('-' * 10)
23 print("NY State has: ", cities['NY'])
24 print("OR State has: ", cities['OR'])
25
26 # print some states
27 print('-' * 10)
28 print("Michigan's abbreviation is: ", states['Michigan'])
29 print("Florida's abbreviation is: ", states['Florida'])
30
31 # do it by using the state then cities dict
32 print('-' * 10)
33 print("Michigan has: ", cities[states['Michigan']])
34 print("Florida has: ", cities[states['Florida']])
35
36 # print every state abbreviation
37 print('-' * 10)
38 for state, abbrev in list(states.items()):
39 print(f"{state} is abbreviated {abbrev}")
40
41 # print every city in state
42 print('-' * 10)
43 for abbrev, city in list(cities.items()):
44 print(f"{abbrev} has the city {city}")
45
46 # now do both at the same time
47 print('-' * 10)
48 for state, abbrev in list(states.items
9 print(f"{state} state is abbreviated {abbrev}")
50 print(f"and has city {cities[abbrev]}")
51
52 print('-' * 10)
53 # safely get a abbreviation by state that right not be there
state=states.get("Texas")
if not state:
57 print("Sorry, no Texas.")
58
59 # get a city with a default value
60 city = cities.get('TX', 'Does Not Exist')
61 print(f"The city for the state 'TX' is: {city}")
