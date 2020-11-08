int_list = [10, 7, -5, 11, -33, 2]


def highest_product(input):

	# answer to validate = product of 3 ints
	# additional values to keep track = min of 3 ints
	# all 3 ints = can we simplify = best product of 2
	# negative numbers = highest 1
	
	if len(input) < 3:
		raise ValueError("Sequence not large enough")
		
	
	#additional values
	highest = max(input[0], input[1])
	lowest = min(input[0], input[1])
	
	highest_2prod = input[0]*input[1]
	lowest_2prod = input[0]*input[1]
	
	highest_3prod = input[0]*input[1]*input[2]
	
	for i in range(2, len(input)):
	
		highest_3prod = max(highest_3prod, highest_2prod*input[i], lowest_2prod*input[i])
		
		highest_2prod = max(highest_2prod, highest*input[i], lowest*input[i])
		lowest_2prod = min(lowest_2prod, lowest*input[i], highest*input[i])
		
		highest = max(highest, input[i])
		lowest = min(lowest, input[i])
		
		
		
	return highest_3prod
			
print(highest_product(int_list))			
		
		
	
		
	
		
	
		