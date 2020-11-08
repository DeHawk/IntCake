# binary tree

class BinaryTreeNode(object):

	def __init__(self, value):
	
		self.value = value
		self.left = None
		self.right = None
		
	def insert_left(self, value):
	
		self.left = BinaryTreeNode(value)
		return self.left
		
	def insert_right(self, value):
	
		self.right = BinaryTreeNode(value)
		return self.right
		

# construct tree

# root = BinaryTreeNode(5)
# left = root.insert_left(4)
# right = root.insert_right(6)
# left2 = left.insert_left(3)
# right2 = right.insert_right(7)
# left_right = left.insert_right(2)
# right_left = right.insert_left(8)

tree = BinaryTreeNode(5)
left = tree.insert_left(8)
right = tree.insert_right(6)
left.insert_left(1)
left.insert_right(2)
right.insert_left(3)
right.insert_right(4)

# depth function

# first write for largest

def find_largest(root):

	current = root
	
	while current:
	
		if not current.right:
			return current.value
			
		current = current.right
		

def find_second_largest(root):

	if not root or (if not root.left and if not root.right):
	
		raise ValueError('Need atleast 2 nodes')
		
	
	current = root
	
	while current:
	
		if current.left and not current.right:
			return find_largest(current.left)
			
		if current.right and not current.right.left and not current.right.right:
			return current.value
			
		current = current.right
		

	

print(depth_check(tree))
	
		
