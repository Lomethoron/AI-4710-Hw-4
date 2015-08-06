from negotiator_base import BaseNegotiator
from random import random, shuffle


class wwd9d(BaseNegotiator):

    def __init__(self):
        BaseNegotiator.__init__(self)
        self.turn_counter = 0
        self.their_last_offer_utility = 0
        self.results = 0
        self.is_first = False
        # time at which we think we have a reasonable grasp on their offer
        self.turn_model_becomes_accurate = self.iter_limit*.20
        # container of probabilities
        self.mastermind_probabilities = []

        # temp testing
        print "pref in init is ", self.preferences
        self.offer = list(reversed(self.preferences))
        print "Wrongest order nets us ", self.utility()

    def make_offer(self, offer):
        print "\nOur Negotiator:"

        # temp testing
        print "pref in init is ", self.preferences
        self.offer = list(reversed(self.preferences))
        print "Wrongest order nets us ", self.utility()
        # temp to make sure we are offering something
        self.offer = self.preferences
        print "We recieve exactly ", self.utility(), " for our best offer"
        # turn counter
        # is it not the first turn
        if offer:
            self.turn_counter += 1
            self.offer = offer
            print "We recieve exactly ", self.utility(), " for their offer"
        # if it is the first turn
        else:
            self.turn_counter = 1
            self.is_first = True

        # init probability holder
        if self.turn_counter == 1:
            for position in self.preferences:
                tempMap = dict()
                times_looped = 0
                for type in self.preferences:
                    tempMap[type] = 0
                    times_looped += 1
                self.mastermind_probabilities.append(tempMap)
                print "times looped ", times_looped
        #print "mastermind probabilities initialized ", self.mastermind_probabilities


        # accept offer
        print "Incoming offer ", self.offer
        print "Our best ordering ", self.preferences

        # if it is our best, take it
        if self.compare(self.preferences, self.offer):
            print "best offer"
            self.offer = offer
            self.turn_counter = 0
            return self.offer

        # last turn price protection
        # we expect that on the last turn the opponent will attempt to send a bad deal
        # this attempts to dodge that, accepting a slight penalty to avoid this
        if (self.iter_limit-1) == self.turn_counter and not self.is_first:
            print "last turn dodge"
            # make sure offer is worthwhile for us
            # penalty is - the length of the ordering
            if self.their_last_offer_utility > -len(offer):
                # take the last offer
                self.offer = offer
                self.turn_counter = 0
                return self.offer

        # last turn acceptance, just in case
        if self.iter_limit == self.turn_counter:
            print "last turn acceptance\n"
            if self.their_last_offer_utility > -len(offer):
                # take the last offer
                self.offer = offer
                self.turn_counter = 0
                return self.offer
        # temp last turn acceptance
        if self.iter_limit == self.turn_counter:
            print "edge case hit"
            self.offer = offer
            self.turn_counter = 0
            return self.offer

        # general acceptance
        # figure out if deal is worth it to accept

        # reject offer
        # how to form a good counter-offer

    def receive_utility(self, curr_utility):
        self.their_last_offer_utility = curr_utility

    def receive_results(self, results):
        self.results = results

    def compare(self, list_a, list_b):
        is_same = True
        #print len(list_b)
        #print len(list_a)
        if len(list_b) == len(list_a):
            for elem_a in list_a:
                for elem_b in list_b:
                    if elem_a != elem_b:
                        is_same = False
        else:
            is_same = False
        return is_same

    # swaps offer with a new offer value to test its value, returns it after value is found
    def get_curr_util(self, new_ordering):
        temp = self.offer
        self.offer = new_ordering
        now_util = self.utility()
        self.offer = temp
        return now_util

