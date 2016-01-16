from random import randint, shuffle


def main():
    gameobject = Game()
    gameobject.game_setup()


    # Loop through the steps of playing the game until someone wins
    while gameobject.gamestate != "WINNERFOUND":
        # first have them roll onces
        while gameobject.gamestate != "CHANGETURN":
            gameobject.roll_dice()

            # Check game state
            gameobject.check_game()

            # Ask if they want to roll again
            if gameobject.ask_player() == False:
                break
        # if no, go to next player turn
        gameobject.next_turn()

        ##in next turn tell the person it's their turn



class Die():

    def __init__(self, color):
        self.color = color

        if color == 6:
            self.sides = [["B"],["B"],["B"],["F"],["F"],["S"]]
        elif color == 4:
            self.sides = [["B"],["B"],["F"],["F"],["S"],["S"]]
        elif color == 3:
            self.sides = [["B"],["F"],["F"],["S"],["S"],["S"]]

        self.currentvalue = self.sides[0]

    def roll(self):
        shuffle(self.sides)
        self.currentvalue = self.sides[0]

    def __repr__(self):
        return "{}".format(self.currentvalue)


class Game():
    def __init__(self):
        self.playerobjectlist = []
        self.current_player = 0
        self.gamestate = 0
        self.rownd = 0
        self.thirteen_dice = [Die(6),Die(6),Die(6),Die(6),Die(6),Die(6),Die(4),Die(4),Die(4),Die(4),Die(3),Die(3),Die(3)]
        shuffle(self.thirteen_dice)
        self.current_dice = []
        self.cup = []
        self.brains = []
        self.brainCount = 0
        self.shotguns = []



    def roll_dice(self):

        # Figure out how many die we need
        num = 3 - len(self.current_dice)
        # Grab a new die for every die we're missing
        while num > 0:
            # Make sure we have enough dice in the cup before grabbing one
            if len(self.cup) == 0:
                self.cup = self.brains
                self.brains = []
                shuffle(self.cup)
            self.current_dice.append(self.cup.pop())
            num -= 1

        copy = self.current_dice
        for die in copy:
            die.roll()
            if die.currentvalue == ["B"]:
                self.brainCount += 1
                self.brains.append(die)
                self.current_dice.remove(die)
            elif die.currentvalue == ["S"]:
                self.shotguns.append(die)
                self.current_dice.remove(die)



    def check_game(self):
        if len(self.shotguns) == 3:
            print ("Sorry you just got shot.")
            self.gamestate = "CHANGETURN"
        elif len(self.brains) == 13:
            print ("You Won!!!")
            self.gamestate = "WINNERFOUND"

    def ask_player(self):
        ask = input("Do you want to roll again? Y or N ")
        if ask == "Y":
            return True
        elif ask == "N":
            return False
        else:
            ask_player()


    def next_turn(self):
        if self.current_player < len(self.playerobjectlist)-1:
            self.current_player += 1
        else:
            self.current_player = 0
        self.cup = self.thirteen_dice
        shuffle(self.cup)
        self.current_dice = []

    def game_setup(self):
        self.cup = self.thirteen_dice
        shuffle(self.cup)
        wanna_play = int(input("How many players? (Please enter a number between 1 and 6):"))
        if wanna_play <= 6 and wanna_play != 0:
            self.name_setup(wanna_play)
        else:
            print("Sorry please enter a number between 1 and 6")
            game_setup()


    def name_setup(self, numberofplayers):
        for x in range(1, (numberofplayers + 1)):
            print ("Player number" + str(x))
            name = input("Please enter name:")
            self.playerobjectlist.append(Player(name))


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
        gameobject.playerobjectlist.append(Player(name))



if __name__ == '__main__':
    main()
