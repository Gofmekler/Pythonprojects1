# birthdays paradox
from random import *
from datetime import *


# returns list of random birthdays dates
def GetBirthdays(numberOfBirthdays):
    birthdays = []
    for p in range(numberOfBirthdays):
        startOfYear = date(2001, 1, 1)
        randomNumberOfDays = timedelta(randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, BirthdayA in enumerate(birthdays):
        for b, BirthdayB in enumerate(birthdays[a + 1:]):
            if BirthdayA == BirthdayB:
                return BirthdayA


print("Paradox surprising")

Month = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
while True:
    print("How many birthdays shall i generate?")
    responce = input('> ')
    if responce.isdecimal() and (0 < int(responce) < 100):
        numBdays = int(responce)
        break
print()
print("Here are", numBdays, "birthdays")
birthdays = GetBirthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(',', end='')
    monthName = Month[birthday.month - 1]
    dataText = '{}{}'.format(monthName, birthday.day)
    print(dataText, end='')
print()
print()
match = getMatch(birthdays)
print('In this simulat,', end='')
if match is not None:
    monthName = Month[match.month - 1]
    dataText = "{}{}".format(monthName, match.day)
    print("multiple people have a birthday on", dataText)
else:
    print("there are no match")
print()
print("Generating", numBdays, " random bday 100000 times..")
input("press enter to begin ")
print("another 100000 simulations")
simMatch = 0
for i in range(100000):
    if i % 10000 == 0:
        print(i, "simulations run..")
    birthdays = GetBirthdays(numBdays)
    if getMatch(birthdays) is not None:
        simMatch = simMatch + 1
print("100000 simulations run")
probability = round(simMatch / 100000 * 100, 2)
print("out of 100000 simulations of", numBdays, "people, there was a")
print("matching bdays in that group", simMatch, " times")
