#Guess the number game
from random import randint

#define func which choices the comp num
def comput_num(min_num,max_num):
    return randint(min_num,max_num)


def player_propose(min_num,max_num):
    user_input = int(input(f'guess the number between {min_num} and {max_num}: '))
    try:
        if user_input in range(min_num,max_num):
            return user_input
        else:
            raise TypeError
    except TypeError:
        print("invalid")

#Define func which returns players choice with exceptions
# def player_propose(min_num,max_num):
#     while True:
#         try:
#             user_input = int(input(f'guess the number between {min_num} and {max_num}: '))
#             while user_input >= min_num or user_input <= max_num:
#                 return user_input
#             else:
#
#                 raise ValueError  # this will send it to the print message and back to the input option
#                 break
#         except ValueError:
#             print(f"Invalid integer. The number must be in the range of {min_num} to {max_num}")


#Define game system
def play ():

    low = int(input("Lowest: "))
    high = int(input("Highest:"))
    comput_choice = comput_num(low, high)
    player_choice = player_propose(low, high)
    #Loop until winning
    while player_choice != comput_choice:
        if player_choice > comput_choice:
            player_choice = int(input("Too high, try again : "))
        elif player_choice < comput_choice:
            player_choice = int(input("Too low, try again : "))


    print(f'Congrats, you managed the number {comput_choice}')

#Starts game
play()