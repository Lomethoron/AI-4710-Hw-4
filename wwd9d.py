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
        self.their_previous_offer_utility = 0
        self.current_guess = []
        self.optimal_solution_guess = []
        self.last_guess = []

        # temp testing

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
                    tempMap[type] = 0.0
                    times_looped += 1
                self.mastermind_probabilities.append(tempMap)
        # print "mastermind probabilities initialized ", self.mastermind_probabilities

        # take incoming offer and update probabilities
        is_new_deal_better_for_opponent = True
        if self.their_last_offer_utility < self.their_previous_offer_utility:
            is_new_deal_better_for_opponent = False

        # update the previous offer utility for next turn
        self.their_previous_offer_utility = self.their_last_offer_utility

        # set up weight for updating the prob
        prob_weight = 1.0/self.turn_counter


        # if the opponenets utility goes up, weight that ordering higher
        if is_new_deal_better_for_opponent and self.turn_counter > 1:
            prob_weight *= (self.turn_counter/(self.turn_counter-1.0))
        else:
            prob_weight = 1.0

        # update the probs
        if not self.is_first or self.turn_counter>1 :
            temp_position = 0
            temp_max_value = ""
            for position in self.mastermind_probabilities:
                # update prob
                key_to_be_edited = position.get(offer[temp_position])
                key_to_be_edited += prob_weight
                position[offer[temp_position]] = key_to_be_edited

                # store prob

                temp_position += 1

            # print "mastermind probabilities updated ", self.mastermind_probabilities

            # build best guess
            self.current_guess = []
            for position in self.mastermind_probabilities:
                choice = ""
                prob = 0
                for value in iter(position):
                    if value not in self.current_guess and prob < position.get(value):
                        choice = value
                        prob = position.get(value)
                self.current_guess.append(choice)

        # build optimal solution
        self.optimal_solution_guess = []
        temp_position = 0
        print "preferences ", self.preferences
        print "current guess ", self.current_guess
        print "zip ", zip(self.preferences, self.current_guess)
        for our_ordering, their_ordering in zip(self.preferences, self.current_guess):
            our_distance = abs(self.preferences.index(their_ordering) - temp_position)
            their_distance = abs(self.current_guess.index(our_ordering) - temp_position)
            print "our distance ", our_distance, " their distance ", their_distance
            # if they are the same
            if our_ordering == their_ordering and our_ordering not in self.optimal_solution_guess:
                self.optimal_solution_guess.append(our_ordering)
            # our distance > their distance
            elif our_distance>their_distance and our_ordering not in self.optimal_solution_guess:
                self.optimal_solution_guess.append(our_ordering)
            # their distance > our distance
            elif their_distance>our_distance and their_ordering not in self.optimal_solution_guess:
                self.optimal_solution_guess.append(their_ordering)
            # their distance == our distance
            elif their_ordering not in self.optimal_solution_guess:
                self.optimal_solution_guess.append(their_ordering)
            else:
                self.optimal_solution_guess.append(our_ordering)
            temp_position +=1

        print "best optimal guess ", self.optimal_solution_guess




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

