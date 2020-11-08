# implementing stack class

# push at end, pop at end, peek at end

input = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."


class Stack(object):

	def __init__(self):
		self.items = []
		
	def push(self, value):
		self.items.append(value)
		
	def pop(self):
		if not self.items:
			return None
		return self.items.pop()
		
	def peek(self):
		if not self.items:
			return None
		return self.items[-1]
		
def bbp_validator(input):

	my_stack = Stack()

	for char in input:	
		if char in ['(', '{', '[' ]:
			my_stack.push(char)
		elif char in [')', '}', ']']:
			if not my_stack.items:
				return False
			open_bbp = my_stack.pop()
			if  not ((char == ')' and open_bbp == '(') or  (char == '}' and open_bbp == '{') or (char == ']' and open_bbp == '[')) :
				return False
	if my_stack.items:
		return False
	
	return True
	
print(bbp_validator("{ [ ] ( ) }"))
print(bbp_validator("{ [ ( ] ) }"))
		
			
			

	
			
	
		
			
		

