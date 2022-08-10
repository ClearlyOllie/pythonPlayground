# IN DEVELOPMENT NOT COMPLETE!
#credit to ollie#1459 (discord)
import os, random, time #python module imports

class main(): #main class nesting the game

    class players(): #controls player values & adding new players
        playersTb = []
        def __init__(self, name, cash, position):
            self.name = name
            self.cash = cash
            self.position = position
   
    class vars(): #class nesting game variables - can be edited
        waitTime = 0
        minPlayers = 2
        maxPlayers = 6
        
    def game(wTime, minPlayers, maxPlayers):
        print('Welcome to Monopoly in Python [TERMINAL EDITION]!')
        time.sleep(wTime)
        startOption = input('1. Add new player/n2. Start game/n/nEnter your option: ')
        #match startOption:

main.game(game.vars.waitTime) #run the game

