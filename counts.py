import random
from util import *

class Bot(object):
	def __init__(self):
		self.counts = [1,1,1]
	
	def first_hand(self):
		return random.choice(to_str)
	
	def next_hand(self, input):
		op_hand = to_num[input]
		
		# first update the counts
		self.counts[op_hand] += 1
		
		# use the counts to predict the op's next hand
		my_hand = play_expected(self.counts)
		
		return to_str[my_hand]

# when using exec, use legacy behavior
if __name__ == '__main__':
	if not input:
		bot = Bot()
		output = bot.first_hand()
	else:
		output = bot.next_hand(input)
