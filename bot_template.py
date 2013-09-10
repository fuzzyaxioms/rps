import random

to_num = {'R':0, 'P':1, 'S':2}
to_str = ['R', 'P', 'S']
R, P, S = 0, 1, 2
T, W, L = 0, 1, -1
addh = [[R, P, S], [P, S, R], [S, R, P]] # addh[payoff][hand]
subh = [[T, L, W], [W, T, L], [L, W, T]] # subh[my][op]

# given a distribution over the hands, return the hand that gives the highest expected reward
def play_expected(pd):
	rR, rP, rS = pd[S]-pd[P], pd[R]-pd[S], pd[P]-pd[R]
	if rP > rR:
		if rS > rP:
			return S
		else:
			return P
	elif rS > rR:
		return S
	else:
		return R

class Bot(object):
	def __init__(self):
		pass
	
	def first_hand(self):
		return random.choice(to_str)
	
	def next_hand(self, input):
		return self.seed

# when using exec, use legacy behavior
if __name__ == '__main__':
	if not input:
		bot = Bot()
		output = bot.first_hand()
	else:
		output = bot.next_hand(input)
