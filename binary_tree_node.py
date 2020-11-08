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

# depth function float(-Inf)

def is_binary_tree_balanced(tree):

	node_and_bounds = [(tree, -float('Inf'), float('Inf'))]
	
	while node_and_bounds:
	
		node, lower, upper = node_and_bounds.pop()
		
		if node.value <= lower or node.value >= upper:
		
			return False
			
		else:
		
			if node.left:
				node_and_bounds.append((node.left, lower, node.value))
				
			if node.right:
				node_and_bounds.append((node.right, node.value, upper))

	
				
	return True
	

print(is_binary_tree_balanced(tree))
	
		
