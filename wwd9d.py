from negotiator_base import BaseNegotiator
from random import random, shuffle


class wwd9d(BaseNegotiator):

    def __init__(self):
        BaseNegotiator.__init__(self)
        self.turn_counter = 0
        self.curr_utility = 0
        self.results = 0
        self.is_first = False


    def make_offer(self, offer):
        print "using overloaded method"
        # is it not the first turn
        if offer:
            # calculate a bunch of things
            self.turn_counter += 1
        else:
            self.turn_counter = 1
            self.is_first = True

        # is it the first


        # accept offer
        print self.offer
        print self.preferences

        # if it is our best, take it
        if self.compare(self.preferences, self.offer):
            print "best offer"
            self.offer = offer
            return

        # last turn price protection
        # we expect that on the last turn the opponent will attempt to send a bad deal
        # this attempts to dodge that, accepting a slight penalty to avoid this
        if (self.iter_limit-1) == self.turn_counter and self.is_first:
            print "last turn dodge"
            #make sure offer is worthwhile for us
            #penalty is - the length of the ordering
            if self.utility > -len(offer):
                #take the last offer
                self.offer = offer
                return

        # last turn acceptance, just in case
        if self.iter_limit == self.turn_counter:
            print "last turn acceptance"
            print "len offer"+  len(offer)
            if self.utility > -len(offer):
                #take the last offer
                self.offer = offer
                return
        #temp last turn acceptance
        if self.iter_limit == self.turn_counter:
            print "edge case hit"
            self.offer = offer
            return

        # general acceptance

        # reject offer


    def receive_utility(self, curr_utility):
        self.curr_utility = curr_utility

    def receive_results(self, results):
        self.results = results

    def compare(self, list_a, list_b):
        is_same = True
        print len(list_b)
        print len(list_a)
        if len(list_b) == len(list_a):
            for elem_a in list_a:
                for elem_b in list_b:
                    if elem_a != elem_b:
                        is_same = False
        else:
            is_same = False
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
