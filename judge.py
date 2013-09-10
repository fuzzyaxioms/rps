import random, time, itertools, math

# config options
ROUNDS = 1000
GAMES = 100

# my vs op
cmp_hands = {
	'R':{'R':0, 'P':-1, 'S':1},
	'P':{'R':1, 'P':0, 'S':-1},
	'S':{'R':-1, 'P':1, 'S':0}
}

# m1, and m2 are the two modules following the template
def play_game(m1, m2):
	# initialization and resets
	random.seed(0)
	scores = [None] * GAMES
	start_time = time.clock()
	
	for i in xrange(GAMES):
		b1, b2 = m1.Bot(), m2.Bot()
		payoffs = [0, 0, 0]
		
		# first round
		h1, h2 = b1.first_hand(), b2.first_hand()
		payoffs[cmp_hands[h1][h2]] += 1
		
		for j in xrange(1,ROUNDS):
			h1, h2 = b1.next_hand(h2), b2.next_hand(h1)
			payoffs[cmp_hands[h1][h2]] += 1
		
		# keep track of the result of the game
		scores[i] = payoffs[1] - payoffs[-1]
		
		#print('Game {}, Score {}'.format(i, payoffs[1] - payoffs[-1]))
	
	end_time = time.clock()
	
	wins = [s for s in scores if s > 0]
	ties = [1 for s in scores if s == 0]
	losses = [-s for s in scores if s < 0]
	
	mean_wins = (float(sum(wins)) / len(wins)) if wins else float('nan')
	mean_losses = (float(sum(losses)) / len(losses)) if losses else float('nan')
	
	diffs_wins = math.sqrt(sum((s-mean_wins)*(s-mean_wins) for s in wins)/len(wins)) if wins else float('nan')
	diffs_losses = math.sqrt(sum((s-mean_losses)*(s-mean_losses) for s in losses)/len(losses)) if losses else float('nan')
	
	print('{} vs {}'.format(m1.__name__, m2.__name__))
	print('    W: {:4}/{} | {:7.2%} | {:7.2f}{:7.2f}'.format(len(wins), GAMES, float(len(wins))/GAMES, mean_wins, diffs_wins))
	print('    T: {:4}/{} | {:7.2%}'.format(len(ties), GAMES, float(len(ties))/GAMES))
	print('    L: {:4}/{} | {:7.2%} | {:7.2f}{:7.2f}'.format(len(losses), GAMES, float(len(losses))/GAMES, mean_losses, diffs_losses))
	print('    {:.2f}ms'.format((end_time-start_time)*1000/GAMES))

if __name__ == '__main__':
	import constant, beat_last, counts
	play_game(beat_last, counts)
