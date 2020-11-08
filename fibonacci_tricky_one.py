
# recursive permutation

# star, 

# 0 1 1 2 3 5 8

def do_fibonacci(n):

	if n < 0:
		raise IndexError('No negative index')
	elif n in [0,1]:
		return n
	
	a,b = 0, 1
	
	for i in range(2, n):
		c = a + b
		a = b
		b = c
		
		
	return c
	

print(do_fibonacci(5))
	
		
	