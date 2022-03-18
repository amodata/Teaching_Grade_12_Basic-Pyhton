my_list = ["apple", "cherry", "lemon"]
my_dict = {"drink": "coffee", "milk": "whole"}

for item in my_list:
    print(f"My favorite thing to eat is: {item}")

for key, value in my_dict.items():
    print(f"My favorite thing to drink is {key} : {value}")
for _, value in my_dict.items():
    print(f"My favorite thing to drink is: {value}")

# Potential errors below
# Create a test to catch the below issues
# my_dict=my_dict
# my_list2=
