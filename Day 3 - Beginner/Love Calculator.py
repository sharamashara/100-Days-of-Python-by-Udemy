print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
combie_names = name1 + name2

t = combie_names.count("t")
r = combie_names.count("r")
u = combie_names.count("u")
e = combie_names.count("e")
num1=t+r+u+e
l = combie_names.count("l")
o = combie_names.count("o")
v = combie_names.count("v")
e = combie_names.count("e")
num2=l+o+v+e

num = int(str(num1)+str(num2))

if num <= 10 or num >=90:
    print(f"Your score is {num}, you go together like coke and mentos.")
elif num >= 40 and num <= 50:
    print(f"Your score is {num}, you are alright together.")
else:
    print(f"Your score is {num}.")