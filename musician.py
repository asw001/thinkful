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

    def starter_count(self):
        print("A-one, two, three, four!")
        print()

    def combust(self):
        print("Wha! I'm on fiyaaaaaahh!")

class Band(object):
    def __init__(self, name, members):
        self.nane = name
        self.members = members

    def play(self):
        members = self.members
        print(members)
        for member in members.values():
            if isinstance(member, Drummer):
                member.starter_count()

        for player in members.values():
            player.solo(random.choice(range(1,8)))


