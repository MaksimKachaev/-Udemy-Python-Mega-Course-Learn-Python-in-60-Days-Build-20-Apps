from parsers import parse
import random

# Ask the user to enter a lower and an upper bound divided by a comma
user_input = input("Enter a lower bound and an upper bound divided a comma (e.g., 2,10) ")

# Parse the user string by calling the parse function
parsed = parse(user_input)

# Pick a random int between the two numbers
rand = random.uniform(parsed['lower_bound'], parsed['upper_bound'])

print(round(rand, 3))





















# from parsers import parse
# import random
#
# # Ask the user to enter a lower and an upper bound divided by a comma
# user_input = input("Enter a lower bound and an upper bound divided a comma (e.g., 2,10)")
#
# # Parse the user string by calling the parse function
# parsed = parse(user_input)
#
# # Pick a random int between the two numbers
#
# print(f"{parsed['lower_bound']} {parsed['upper_bound']}")
# rand = random.uniform(parsed['lower_bound'], parsed['upper_bound'])
#
# print(rand)
