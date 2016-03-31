#!/usr/bin/python3

import random

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Rat-a-tat", "Kisshhh!", "Thump"])

    def tune(self):
        print("Be with you in a moment")
        print("Tap-tap, thump, whoomp")

    def count(self):
        print("A-one, two, three, four!")

    def combust(self):
        print("Wha! I'm on fiyaaaaaahh!")

class Band(object):
    def __init__(self, name):
        self.nane = name

    def play(self, members):

        lineup = []

        for member in members.values():
            print(member)
            if isinstance(member, Drummer):
                lineup.insert(0, member)
            else:
                lineup.append(member)

        print(lineup)
        for player in lineup:
            player.solo(random.choice(range(8)))

if __name__ == '__init__':
    theband = Band("The Destroyers")
    members = {"jeff": Guitarist(), "don": Bassist(), "alia": Drummer()}
    theband.play(members)
