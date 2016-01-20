from random import randint, shuffle
import time

def main():
    gameobject = Game()
    gameobject.game_setup()
    # Loop through the steps of playing the game until someone wins
    while gameobject.gamestate != "WINNERFOUND":
        gameobject.roll_dice()
        gameobject.check_game()
        if gameobject.gamestate == "CHANGETURN":
            gameobject.next_turn()
            continue
        elif gameobject.gamestate != "CHANGETURN":
            if gameobject.ask_player() == False:
                gameobject.next_turn()
            else:
                continue

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
#takes used fie from cup and adds to current_dice
            self.current_dice.append(self.cup.pop())
            num -= 1
#creates a copy of current dice
        copy = self.current_dice[:]
#for loop for the current dice copy, runs the die.roll function which determines
#whether each die represents a foot, brain, or shotgun
        for die in copy:
            die.roll()
#adjusts the brain count and brain list
            if die.currentvalue == ["B"]:
                self.playerobjectlist[self.current_player].brainCount += 1
                self.brains.append(die)
                self.current_dice.remove(die)
#adjusts the shotgun count
            elif die.currentvalue == ["S"]:
                self.shotguns.append(die)
                self.current_dice.remove(die)
        time.sleep(1)
        print(str(self.playerobjectlist[self.current_player]))
        time.sleep(.5)
        print("You have just rolled,")
        print(copy)
        print("For this turn you have {} brains and {} shotguns".format(len(self.brains), len(self.shotguns)))
        print("Total brains this game {}".format(self.playerobjectlist[self.current_player].brainCount))

    def check_game(self):
        if len(self.shotguns) >= 3:
            print ("You have been shot 3 times! YOUR TURN IS OVER")
            self.gamestate = "CHANGETURN"
            self.playerobjectlist[self.current_player].brainCount = self.playerobjectlist[self.current_player].brainCount - len(self.brains)

        elif self.playerobjectlist[self.current_player].brainCount >= 13:
            print ("You Won!!! GAME OVER")
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
        self.cup = self.thirteen_dice[:]
        shuffle(self.cup)
        self.current_dice = []
        self.shotguns = []
        self.brains = []
        self.gamestate = 0

    def game_setup(self):
        self.cup = self.thirteen_dice[:]
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
        self.brainCount = 0

    def __str__(self):
        return "{}".format(self.name)

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
