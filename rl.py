import random
from util import *
import cPickle

params = '(dp1\n.'

class Bot(object):
    def __init__(self):
        if params is None:
            self.params = {}
        else:
            self.params = cPickle.loads(params)

    def first_hand(self):
        return random.choice(to_str)

    def next_hand(self, input):
        return self.seed

# when using exec, use legacy behavior
if __name__ == '__main__':
    #if not input:
	#    bot = Bot()
	#    output = bot.first_hand()
    #else:
	#    output = bot.next_hand(input)
    
    # try out other stuff
    bot = Bot()
    print(repr(bot.params))
    print(repr(cPickle.dumps(bot.params)))
