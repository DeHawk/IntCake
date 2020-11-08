
# without memoization

def fibonacci(n):

	if n < 0:
		raise IndexError("No negative index in fibonacci")
	elif n in [0,1]:
		return n
		
	print(f"Computing fib of {n}")
	return fibonacci(n-1) + fibonacci(n-2)

# with memoization

class Fibonacci:

	def __init__(self):
		self.memo = {}
		
	def compute_fibonacci(self, n):
		if n < 0:
			raise IndexError("No negative index in fibonacci")
		elif n in [0,1]:
			return n
			
		if n not in self.memo:
			result = self.compute_fibonacci(n-1) + self.compute_fibonacci(n-2)
			self.memo[n] = result
			print(f"computing fib of {n}")
			
		else:
			result = self.memo[n]
			
		return result
			
			
		
		
#without memoization
print(fibonacci(10))
print(Fibonacci().compute_fibonacci(10))