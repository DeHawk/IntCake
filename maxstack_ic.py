# implementing stack class

# push at end, pop at end, peek at end


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

		
		
class MaxStack(object):

	def __init__(self):
		self.stack = Stack()
		self.max_stack = Stack()
		
	def push(self, value):
		self.stack.push(value)
		if not self.max_stack.peek() or value >= self.max_stack.peek():
			self.max_stack.push(value)
			
	def pop(self):
		item = self.stack.pop()
		if item == self.max_stack.peek():
			self.max_stack.pop()
		return item		
		
	def get_max(self):
		return self.max_stack.peek()
		
		
stack1 = MaxStack()
stack1.push(3)
stack1.push(5)
stack1.push(1)
stack1.push(2)
stack1.push(10)
stack1.push(4)

print(stack1.get_max())




	
	
			
		

