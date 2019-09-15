# Actor.py
# Author(s): Phillip Tran

# first party
import random

class Actor:
    def __init__(self, avaliable_funds: int, lower_threshhold:int, betrayal_rate:float):
        '''
        :param avaliable_funds: The amount of money the actor has avaliable
        :param lower_threshhold: The lowerest that the avaliable funds can be before the betrayal_rate starts increasing
        :param betrayal_rate: A value between 0 and 1 that determines how likely the actor is to betray
        :type avaliable_funds: int
        :type lower_threshhold: int
        :type betrayal_rate: float
        :return None
        '''
        self.avaliable_funds = avaliable_funds
        self.lower_threshhold = lower_threshhold
        self.betrayal_rate = betrayal_rate

    def make_choice(self):
        '''
        This function will make a choice by randomly selecting a number between 0
        and 1 and see if that number is greater than the betrayl rate. If it is,
        return 'Trust' if not return 'Betray'
        :return: 'Trust' or 'Betray'
        :rtype: string
        '''
        r = random.uniform(0,1)
        print(r)
        if r > self.betrayal_rate:
            return "Trust"
        else:
            return "Betray"

    def update(self):
        if self.avaliable_funds < self.lower_threshhold:
            self.betrayal_rate += .05
        else:
            self.betrayal_rate -= .05
