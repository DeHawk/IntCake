import random

def get_random(floor, ceiling):
	return random.randrange(floor, ceiling + 1)



def in_place_shuffle(input):

	if len(input) < 2:
		raise ValueError('List doesnt have adequate length')
		
	last_index = len(input) - 1


	for index_chosen in range(0,last_index):
	
		random_pick = get_random(index_chosen, last_index)
		
		if random_pick != index_chosen:
		
			input[index_chosen], input[random_pick] = input[random_pick], input[index_chosen]
			

inlist = [4,6,2,7,5,3,9]

print('before:', inlist)

in_place_shuffle(inlist)

print('after:',inlist)
	
		
	
	