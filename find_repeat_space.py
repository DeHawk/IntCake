
# find repeat optimize for space

the_list = [3,2,5,4,1,4]

def find_repeat(the_list):

	# consider only the unique possible ints
	
	floor = 1
	ceil = len(the_list) - 1
	
	while floor < ceil :
	
		mid = floor + (ceil-floor)//2
		
		lower_floor, lower_ceil = floor, mid
		upper_floor, upper_ceil = mid+1, ceil
		
		items_in_lower = 0
		
		for item in the_list:
		
			if item >= lower_floor and item <= lower_ceil:
			
				items_in_lower += 1
				
		unique_possible_lower = mid - floor + 1
		
		if items_in_lower > unique_possible_lower:
		
			floor, ceil = lower_floor, lower_ceil
			
		else :
			
			floor, ceil = upper_floor, upper_ceil
			
	
	return floor

print(find_repeat(the_list))	
		
			

