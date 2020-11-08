
# recursive permutation

# star, 

def get_permutation(string):

	if len(string) <= 1:
		return set([string])
		
	string_till_last_char = string[:-1]
	last_char = string[-1]
	
	perms_till_last_char = get_permutation(string_till_last_char)
	
	permutations = set()
	
	for perm in perms_till_last_char:
		for position in range(len(perm)+1):
		
			permutation = (perm[:position] + last_char + perm[position:])
			
			permutations.add(permutation)
			
	return permutations
	

print(get_permutation("cat"))