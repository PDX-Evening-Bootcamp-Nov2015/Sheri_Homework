from randome import randint, shuffle, choice
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
    def __init__(self, name,):
        self.name = name
        self.turn = turn
        self.current_shotguns = current_shotguns
        self.current_brains =current_brains
        self.brain_stash

wanna_play = input("How many palyers? (up to six) ")
# whos_playing = input("enter player " player_number "'s name: ")
player_one_name = input("enter player one's name")
player_two_name = input("enter player two's name")


player_one = Player(player_one_name, 0, 0, 0, 0)
player_two = Player(player_two_name, 0, 0, 0, 0)

def roll_die():
    die_list=[g, g, g, g, g, g, y, y, y, y, r, r, r]
    chosen_die = shuffle(die_list)
    chosen_die.pop

shuffle(game.the_cuo)
self.blah = game.blah[:3]
