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
		

class QueueTwoStacks(object):

	def __init__(self):
		self.in_stack = Stack()
		self.out_stack = Stack()
		
	def enqueue(self, value):
		self.in_stack.push(value)
		
	def dequeue(self):
		if not self.out_stack.items:
			while self.in_stack.items:
				self.out_stack.push(self.in_stack.pop())
			if not self.out_stack.items:
				raise ValueError("No items in queue to pop out")
				
		return self.out_stack.pop()
		
		
		
			
		

