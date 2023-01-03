# Pencil Game - With JACK being a ROBOT Player
# David A. King Jan 3, 2023 - ALL MY CODE
# JetBrains Academy Challenge Project
import random

pencils = ""
tempname = ""
take_pencils = (1, 2, 3)
winpos = False


def nextplayer(playersname):
    if playersname == 'John':
        return 'Jack'
    else:
        return 'John'


def dowinner():
    global nextname
    print(f"{nextname} won!")
    exit()


# Real Human Player - takes some pencils
def getpencilchoice():
    global pencils
    getpencils = True
    while getpencils:
        pen_taken = input()
        if not pen_taken.isdigit():
            print("Possible values: '1', '2' or '3'")
            continue
        elif int(pen_taken) not in take_pencils:
            print("Possible values: '1', '2' or '3'")
            continue
        elif int(pen_taken) > pencils:
            print("Too many pencils were taken")
            continue
        else:
            pencils = int(pencils) - int(pen_taken)

        if pencils == 0:  # Game ver
            dowinner()
        else:
            getpencils == False
        return


def robotplay():
    global pencils
    takepen = 0

    if pencils > 0:

        if pencils % 4 == 0:
            takepen = 3
            pencils -= 3
        elif pencils % 4 == 3:
            takepen = 2
            pencils -= 2
        elif pencils % 4 == 2:
            takepen = 1
            pencils -= 1
        elif pencils % 4 == 1:
            takepen = 1
            pencils -= 1

        print(takepen)

        if pencils == 0:  # Game ver
            dowinner()


    else:
        if pencils > 3:
            toprange = 3
        else:
            toprange = pencils
        pentake = random.randint(1, toprange)
        print(pentake)
        pencils -= pentake

    if pencils == 0:  # Game ver
        dowinner()


# start the game, set up the starting pencils and first user
pencil_input_test = True
print("How many pencils would you like to use:")
while pencil_input_test:

    pencils = input()

    if not pencils.isdigit():
        print("The number of pencils should be numeric")
        continue
    elif int(pencils) == 0:
        print("The number of pencils should be positive")
        continue
    elif int(pencils) < 0:
        print("The number of pencils should bbb be numeric")
        continue
    else:
        pencils = int(pencils)
        pencil_input_test = False

# get first player name
checkname = True
print("Who will be the first, (John, Jack):")
while checkname:
    name = input().lower()

    if name == 'jack':
        winpos = True

    if name == 'john' or name == 'jack':
        checkname = False

    else:
        print("Choose between 'John' or 'Jack'")
        continue

print("|" * pencils)
playing_name = name.title()
nextname = nextplayer(playing_name).title()

while pencils > 0:

    print(f"{playing_name}'s turn!")
    if playing_name == "Jack":
        robotplay()
    else:
        getpencilchoice()

    tempname = playing_name
    playing_name = nextname
    nextname = tempname
    print("|" * pencils)