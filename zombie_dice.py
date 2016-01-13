import random

class Die():

    def __init__(self, color, brain, gun, feet, hold):
        self.color = color
        self.brain = brain
        self.gun = gun
        self.feet = feet
        self.hold = False

class Game():
    def __init__(self, whose_turn):
        self.whose_turn = whose_turn
        self.rownd = 0
        self.green_die = 6
        self.yellow_die = 4
        self.red_die = 3

class Player():
    def __init__(self, name, turn, current_shotguns, current_brains, brain_stash):
        self.name = name
        self.turn = turn
        self.current_shotguns = current_shotguns
        self.current_brains = current_brains
        self.brain_stash = brain_stash

    def __str__(self):
        return "{}, Brains ={}".format(self.name, self.brain_stash)

def game_setup():
    wanna_play = int(input("How many players? (Please enter a number between 1 and 6):"))
    if wanna_play <= 6 and wanna_play != 0:
        name_setup(wanna_play)
    else:
        print("Sorry please enter a number between 1 and 6")
        game_setup()

playernamelist = []
playerobjectlist = []

def name_setup(numberofplayers):
    for x in range(1, (numberofplayers + 1)):
        print ("Player number" + str(x))
        name = input("Please enter name:")
        playernamelist.append(name)
        assign_names_object(playernamelist)

def assign_names_object(playernamelist):
    for x in playernamelist:
        y = Player(str(x), 0, 0, 0, 0)
        playerobjectlist.append(y)
# import pdb; pdb.set_trace()
game_setup()

print(playerobjectlist)
# for c in playerobjectlist:
#     print(c)


#
# player_one_name = input("enter player one's name")
# player_two_name = input("enter player two's name")
#
#
# player_one = Player(player_one_name, 0, 0, 0, 0)
# player_two = Player(player_two_name, 0, 0, 0, 0)
#
#
# def roll_die():
#     die_list=[g, g, g, g, g, g, y, y, y, y, r, r, r]
#     chosen_die = shuffle(die_list)
#     chosen_die.pop
#
# random.shuffle(game.the_cuo)
# self.blah = game.blah[:3]
