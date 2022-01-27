#Another game
from random import *
def users_interface(options):
    for index, option in enumerate(options):
        print(f"{index} = {option}")
    user_input = int(input("Whats your choice? "))
    return user_input
def comp_choice(content):
    comp_choose = randint(0, len(content)-1)
    