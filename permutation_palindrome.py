

text = 'civic'

# parity check = 1 or 0 elems should be occuring even times

def palidrome_check(s):

	track_set = set()
	
	for elem in s:
	
		if elem in track_set:
			track_set.remove(elem)
		else:
			track_set.add(elem)
			
	if len(track_set) > 1 :
		return False
		
	return True
	
print(palidrome_check(text))
			
