# 0, 1, 2, 3, 4, 5 - index or amount
# 1, 1, 1, 1, 1, 1 - # of ways using 1 cent
# 1, 1, 2, 2, 3, 3 - # of ways using 1 and 2 cents

def change_possibilities(amount, denominations):

	ways_to_make_n_cents = [0]*(amount+1)
	
	ways_to_make_n_cents[0] = 1
	
	for coin in denominations:
	
		for higher_amount in range(coin, amount+1):
		
			amount_rest = higher_amount - coin
			
			ways_to_make_n_cents[higher_amount] += ways_to_make_n_cents[amount_rest]
			
	return ways_to_make_n_cents[amount]
	

print(change_possibilities(5,[1,3,5]))
	
	