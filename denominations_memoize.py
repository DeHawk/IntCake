

class Denominate:

	def __init__(self):
		self.memo = {}
		
	
	def denominate(self, amount, denominations, current_index=0):

		memo_key = str((amount, current_index))
		
		if memo_key in self.memo:
			print(f"grabbing {amount} with {current_index} from memo")
			return self.memo[memo_key]
			
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
		
			possibilities += self.denominate(amount, denominations, current_index+1)
			
			amount -= current_coin
			
		self.memo[memo_key] = possibilities
		
		return possibilities
	
print(Denominate().denominate(4,[1,2,3]))
			