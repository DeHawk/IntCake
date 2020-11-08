# implementing stack class

# push at end, pop at end, peek at end

input = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."


def get_nested_paranthesis_close_position(input, position_of_open_paranthesis):

	num_open_nested_paranthesis = 0
	
	for i in range(position_of_open_paranthesis+1,len(input)):
		char = input[i]
		
		if char == "(":
			num_open_nested_paranthesis += 1
		elif char == ")":
			if num_open_nested_paranthesis == 0:
				return i
			else:
				num_open_nested_paranthesis -= 1
	
	raise Exception("No closing paranthesis")
	

print(get_nested_paranthesis_close_position(input, 10))
	
			
	
		
			
		

