from negotiator_base import BaseNegotiator
from random import random, shuffle


class wwd9d(BaseNegotiator):

    def __init__(self):
        super.__init__()
        turnCounter = 0
        utility = 0
        results = 0


    def make_offer(self, offer):
        # is it not the first turn
        if offer:
            # calculate a bunch of things
            self.turnCounter += 1
        else:
            turnCounter = 0

        # is it the first


        # accept offer
        print self.offer
        print self.preferences

        # if it is our best, take it
        if self.compare(self, self.preferences, self.order):
            self.offer = offer
            return

        # last turn price protection
        if (self.iter_limit-1) == turnCounter:
            #make sure offer is worthwhile for us
        # general acceptance

        # reject offer

    def receive_utility(self, utility):
        self.utility = utility

    def receive_results(self, results):
        self.results = results

    def compare(self, list_a, list_b):
        is_same = True
        for elem_a in list_a:
            for elem_b in list_b:
                if elem_a == elem_b:
                    isSame = False
        return is_same

        #  if random() < 0.05 and offer:
        # # Very important - we save the offer we're going to return as self.offer
        #    self.offer = offer[:]
        #   return offer
        # else:
        #   ordering = self.preferences[:]
        #  shuffle(ordering)
        # self.offer = ordering[:]
        # return self.offer
