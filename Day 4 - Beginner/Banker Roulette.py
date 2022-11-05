import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

x = len(names)

random_choise = random.randint(0, x-1)
who_is_pay = names[random_choise]

print(f"{who_is_pay} is going to buy the meal today!")
