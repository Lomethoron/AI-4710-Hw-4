from negotiator_base import BaseNegotiator
from random import random, shuffle

# Example negotiator implementation, which randomly chooses to accept
# an offer or return with a randomized counteroffer.
# Important things to note: We always set self.offer to be equal to whatever
# we eventually pick as our offer. This is necessary for utility computation.
# Second, note that we ensure that we never accept an offer of "None".
class Negotiator(BaseNegotiator):
    # Override the make_offer method from BaseNegotiator to accept a given offer 5%
    # of the time, and return a random permutation the rest of the time.   
    def make_offer(self, offer):
        print "\nDefault Negotiator:"
        self.offer = self.preferences
        tmp_util = self.utility()
        print "The other person recieves exactly ", tmp_util, " for their ideal offer"
        ordering = self.preferences[:]
        shuffle(ordering)
        #self.offer = ordering[:]
        return self.offer
        """
        if random() < 0.05 and offer:
            # Very important - we save the offer we're going to return as self.offer
            self.offer = offer[:]
            return offer
        else:
            self.offer = self.preferences
            tmp_util = self.utility()
            print "The other person recieves exactly ", tmp_util, " for their ideal offer"
            ordering = self.preferences
            shuffle(ordering)
            #self.offer = ordering[:]
            return self.offer
            """
