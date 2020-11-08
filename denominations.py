


def denominate(amount, denominations, current_index=0):

	if amount == 0:
		return 1
		
	if amount <0:
		return 0
		
	if len(denominations) == current_index:
		return 0
		
	print(f"checking ways to make {amount}  with {denominations[current_index:]}")
	
	current_coin = denominations[current_index]
	possibilities = 0
	
	while amount >= 0:
	
		possibilities += denominate(amount, denominations, current_index+1)
		
		print(f"possibilities : {possibilities} for {amount} with current_coin: {current_coin}")
		
		amount -= current_coin
		
	return possibilities
	
print(denominate(4,[1,2,3]))
			