from random import randint, shuffle

class Die():

    def __init__(self):
        self.color = color
        if color == 6:
            self.sides = [["B"],["B"],["B"],["F"],["F"],["S"]]
        elif color == 4:
            self.sides = [["B"],["B"],["F"],["F"],["S"],["S"]]
        elif color == 3:
            self.sides = [["B"],["F"],["F"],["S"],["S"],["S"]]
        shuffle(self.sides)
        self.currentvalue = self.sides[0]


class Game():
    def __init__(self):
        self.playernamelist = []
        self.playerobjectlist = []
        self.whose_turn = 0
        self.rownd = 0
        self.thirteen_dice = [6,6,6,6,6,6,4,4,4,4,3,3,3]
        shuffle(self.thirteen_dice)
        self.spent_dice = []
        self.current_dice = []



        # all_kw.remove(guess)
        # found.append(guess)

class Player():
    def __init__(self, name):
        self.name = name
        self.turn = 0
        self.current_shotguns = 0
        self.current_brains = 0
        self.brain_stash = 0

    def __str__(self):
        return "{}, Brains ={}".format(self.name, self.brain_stash)

    def __repr__(self):
        return "{}, Brains ={}".format(self.name, self.brain_stash)


def game_setup():
    wanna_play = int(input("How many players? (Please enter a number between 1 and 6):"))
    if wanna_play <= 6 and wanna_play != 0:
        name_setup(wanna_play)
    else:
        print("Sorry please enter a number between 1 and 6")
        game_setup()


def name_setup(numberofplayers):
    for x in range(1, (numberofplayers + 1)):
        print ("Player number" + str(x))
        name = input("Please enter name:")
        gameobject.playernamelist.append(name)
    assign_names_object(gameobject.playernamelist)

def assign_names_object(playernamelist):
    for x in playernamelist:
        gameobject.playerobjectlist.append(Player(str(x)))







gameobject = Game()
game_setup()
print(gameobject.playerobjectlist[0].name)


# playerobjectlist[0].turn = 1
# print(playerobjectlist[0].turn)



# player_one_name = input("enter player one's name")
# player_two_name = input("enter player two's name")


# player_one = Player(player_one_name, 0, 0, 0, 0)
# player_two = Player(player_two_name, 0, 0, 0, 0)
