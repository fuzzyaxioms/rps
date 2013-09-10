import random

class Bot(object):
	def __init__(self):
		self.seed = random.choice(['R', 'P', 'S'])
	
	def first_hand(self):
		return self.seed
	
	def next_hand(self, input):
		return self.seed

# when using exec, use legacy behavior
if __name__ == '__main__':
	if not input:
		bot = Bot()
		output = bot.first_hand()
	else:
		output = bot.next_hand(input)
