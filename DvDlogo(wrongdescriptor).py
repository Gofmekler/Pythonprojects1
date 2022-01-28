#DVD LOGO MOVING
import sys
import random
import time

try:
    import bext
except ImportError:
    print("You need to install module Bext, which is required to compilate and run this program")
    sys.exit()
Width, Height = bext.size()
Width -= 1
Number_Of_Logos = 5
Pause_Amount = 0.2
Colors = ['red', 'green', 'blue', 'white', 'cyan', 'black', 'magenta', 'yellow']
Up_Right = 'ur'
Up_Left = 'ul'
Down_Right = 'dr'
Down_Left = 'dl'
Directions = (Up_Right, Up_Left, Down_Right, Down_Left)
Color = 'color'
X = 'x'
Y = 'y'
Dir = 'direction'

def main():
    bext.clear()
    logos = []
    for i in range(Number_Of_Logos):
        logos.append({Color: random.choice(Colors),
                      X: random.randint(1, Width - 4),
                      Y: random.randint(1, Height - 4),
                      Dir: random.choice(Directions)})
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1
    cornerBounces = 0
    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('   ', end='')
            originalDirection = logo[Dir]
            if logo[X] == 0 and logo[Y] == 0:
                logo[Dir] = Down_Right
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == Height - 1:
                logo[Dir] = Up_Right
                cornerBounces += 1
            elif logo[X] == Width - 3 and logo[Y] == 0:
                logo[Dir] = Down_Left
                cornerBounces += 1
            elif logo[X] == Width - 3 and logo[Y] == Height - 1:
                logo[Dir] = Up_Left
                cornerBounces += 1
                # See if the logo bounces off the left edge:
            elif logo[X] == 0 and logo[Dir] == Up_Left:
                logo[Dir] = Up_Right
            elif logo[X] == 0 and logo[Dir] == Down_Left:
                logo[Dir] = Down_Right

            # See if the logo bounces off the right edge:
            # (WIDTH - 3 because 'DVD' has 3 letters.)
            elif logo[X] == Width - 3 and logo[Dir] == Up_Right:
                logo[Dir] = Up_Left
            elif logo[X] == Width - 3 and logo[Dir] == Down_Right:
                logo[Dir] = Down_Left

            # See if the logo bounces off the top edge:
            elif logo[Y] == 0 and logo[Dir] == Up_Left:
                logo[Dir] = Down_Left
            elif logo[Y] == 0 and logo[Dir] == Up_Right:
                logo[Dir] = Down_Right

            # See if the logo bounces off the bottom edge:
            elif logo[Y] == Height - 1 and logo[Dir] == Down_Left:
                logo[Dir] = Up_Left
            elif logo[Y] == Height - 1 and logo[Dir] == Down_Right:
                logo[Dir] = Up_Right
            if logo[Dir] != originalDirection:
                logo[Color] = random.choice(Colors)

            if logo[Dir] == Up_Right:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[Dir] == Up_Left:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[Dir] == Down_Right:
                logo[X] += 2
                logo[Y] += 1
            elif logo[Dir] == Down_Left:
                logo[X] -= 2
                logo[Y] += 1

            bext.goto(5, 0)
            bext.fg("white")
            print("Corner bounces", cornerBounces)
            for logo in logos:
                bext.goto(logo[X], logo[Y])
                bext.fg(logo[Color])
                print("DVD", end='')
            bext.goto(0, 0)
            sys.stdout.flush()
            time.sleep(Pause_Amount)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("boncing dvd logo")
        sys.exit()





