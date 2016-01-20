from random import randint, shuffle
import time

def main():
    """This is the main function. It drives Python Classes."""
    gameobject = Game()
    gameobject.game_setup()
    # Loop through the steps of playing the game until someone wins
    while gameobject.gamestate != "WINNERFOUND":
        gameobject.roll_dice()
        gameobject.check_game()
        # calls next_turn at the right times
        #either when the gamestate is changeturn
        if gameobject.gamestate == "CHANGETURN":
            gameobject.next_turn()
            continue
        #or when the player hits N
        elif gameobject.gamestate != "CHANGETURN":
            if gameobject.ask_player() == False:
                gameobject.next_turn()
            else:
                continue

class Die():
    """This is our die class. It holds all the die properties,
    and the roll method, and returns the die value after the roll"""
    def __init__(self, color):
        self.color = color

        if color == 6:
            self.sides = [["B"],["B"],["B"],["F"],["F"],["S"]]
        elif color == 4:
            self.sides = [["B"],["B"],["F"],["F"],["S"],["S"]]
        elif color == 3:
            self.sides = [["B"],["F"],["F"],["S"],["S"],["S"]]

        self.currentvalue = self.sides[0]
#roll method randomly shuffles the self.sides list and returns current value
    def roll(self):
        shuffle(self.sides)
        self.currentvalue = self.sides[0]
#this method returns the current value of the die after the roll
    def __repr__(self):
        return "{}".format(self.currentvalue)

#game class, with all the game properties
class Game():
    def __init__(self):
        self.playerobjectlist = []
        self.current_player = 0
        self.gamestate = 0
        self.thirteen_dice = [Die(6),Die(6),Die(6),Die(6),Die(6),Die(6),Die(4),Die(4),Die(4),Die(4),Die(3),Die(3),Die(3)]
        shuffle(self.thirteen_dice)
        self.current_dice = []
        self.cup = []
        self.brains = []
        self.shotguns = []

    def roll_dice(self):
        """Roll_dice method inside game class. it also uses shuffle."""

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
#adjusts the shotgun count by appending to self.shotguns. adjusts current dice count.
            elif die.currentvalue == ["S"]:
                self.shotguns.append(die)
                self.current_dice.remove(die)
                #timer so that theres a pause between players
        time.sleep(1)
        #give it a little space
        print("")
        #displays the current player's name
        print(str(self.playerobjectlist[self.current_player]))
        #gives a little time
        time.sleep(.5)
        #displays game info
        print("You have just rolled,")
        print(copy)
        print("For this turn you have {} brains and {} shotguns".format(len(self.brains), len(self.shotguns)))
        print("Total brains this game {}".format(self.playerobjectlist[self.current_player].brainCount))
        #check game method. changes gamestate to CHANGETURN if >3 shotguns
        #or changes it to WINNERFOUND and displays winner messages if 13 brains accumulated
    def check_game(self):
        if len(self.shotguns) >= 3:
            print ("You have been shot 3 times! YOUR TURN IS OVER")
            print(" ")
            self.gamestate = "CHANGETURN"
            self.playerobjectlist[self.current_player].brainCount = self.playerobjectlist[self.current_player].brainCount - len(self.brains)

        elif self.playerobjectlist[self.current_player].brainCount >= 13:
            print ("You Won!!! GAME OVER")
            print (" ")
            self.gamestate = "WINNERFOUND"
        #ask player method. called at each round.
    def ask_player(self):
        x = 0
        while x == 0:
            ask = input("Do you want to roll again? Y or N ")
            if ask.lower() == "y":
                x = 1
                return True
            elif ask.lower() == "n":
                x = 1
                return False
            else:
                x = 0


    def next_turn(self):
        """ next_turn method. Gives each player their turns. selects player turns by going through playerobjectlist
            also resets and shuffles the dice, shotguns, brians and gamestate."""
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
        """gamesetup method. sets up and shuffles dice, asks player to enter number of players"""
        self.cup = self.thirteen_dice[:]
        shuffle(self.cup)
        wanna_play = int(input("How many players? (Please enter a number between 1 and 6):"))
        if wanna_play <= 6 and wanna_play != 0:
            self.name_setup(wanna_play)
        else:
            print("Sorry please enter a number between 1 and 6")
            game_setup()
        # name_setup method. Called by game_setup. displays player number and asks for player names
    def name_setup(self, numberofplayers):
        for x in range(1, (numberofplayers + 1)):
            print ("Player number" + str(x))
            name = input("Please enter name:")
            self.playerobjectlist.append(Player(name))


class Player():
    """Player class. Holds player properties and methods"""
    def __init__(self, name):
        self.name = name
        self.brainCount = 0

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "{}, Brains ={}".format(self.name, self.brain_stash)

if __name__ == '__main__':
    main()
