import random
from util import *

class Bot(object):
	def first_hand(self):
		return random.choice(to_str)
	
	def next_hand(self, input):
		return to_str[addh[W][to_num[input]]]

# when using exec, use legacy behavior
if __name__ == '__main__':
	if not input:
		bot = Bot()
		output = bot.first_hand()
	else:
		output = bot.next_hand(input)
