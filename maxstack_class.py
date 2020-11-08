# implementing stack class

# push at end, pop at end, peek at end


class Stack(object):

	def __init__(self):
	
		self.items = []
		self.max_value = 0
		
	
	def push(self, value):
	
		if not self.items:
			self.max_value = value
		else:
			self.max_value = max(self.max_value, value)			
	
		self.items.append(value)
		
	def pop(self):
	
		if not self.items:
			return None
			
		return self.items.pop()
		
	def peek(self):
	
		if not self.items:
			return None
			
		return self.items[-1]
		
	def get_max(self):
	
		# if not self.items:
			# return None
			
		# max_item = 0
		
		# for i in range(len(self.items)):
		
			# max_item = max(max_item, self.items[i])
			
		return self.max_value
		
stack1 = Stack()
stack1.push(3)
stack1.push(5)
stack1.push(1)
stack1.push(2)
stack1.push(10)
stack1.push(4)

print(stack1.get_max())


	
	
			
		

