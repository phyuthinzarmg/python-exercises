cars = 100
space_in_a_car = 4.0
drivers= 30
passengers =90
cars_not_driven = cars - drivers
cars_drivens = drivers
carpool_capacity = cars_drivens * space_in_a_car
average_passengers_per_car = passenger / cars_driven

print("This is", cars, "cars available.")
print("There are only", drivers," drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity,"people today.")
print("We have", passenger, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

