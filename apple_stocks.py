stock_prices = [10, 7, 5, 4, 3, 2]


def get_max_profit(stock_prices):

	min_val = min(stock_prices[0], stock_prices[1])
	
	max_profit = stock_prices[1] - stock_prices[0]
	
	for i in range(2, len(stock_prices)):
	
		max_profit = max(max_profit, stock_prices[i] - min_val)
		
		min_val = min(min_val, stock_prices[i])
		
	return max_profit
	
print(get_max_profit(stock_prices))
			
			
		
		
	
		
	
		
	
		