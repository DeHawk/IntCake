stock_prices = [10, 7, 5, 4,3,2]


def get_max_profit(stock_prices):
	max_profit = 0

    # Go through every time
	for outer_time in range(len(stock_prices)):

        # For every time, go through every other time
		for inner_time in range(len(stock_prices)):
            # For each pair, find the earlier and later times
			earlier_time = min(outer_time, inner_time)
			later_time   = max(outer_time, inner_time)

            # And use those to find the earlier and later prices
			earlier_price = stock_prices[earlier_time]
			later_price   = stock_prices[later_time]

            # See what our profit would be if we bought at the
            # earlier price and sold at the later price
			potential_profit = later_price - earlier_price

            # Update max_profit if we can do better
			max_profit = max(max_profit, potential_profit)

	return max_profit
	
print(get_max_profit(stock_prices))
	
		