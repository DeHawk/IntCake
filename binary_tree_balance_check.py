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

def depth_check(tree):

	depths = []# capture all depths
	nodes = [] # will hold the tuples - node, depth
	nodes.append((tree,0))
	
	while nodes:
	
		node, depth = nodes.pop()
		
		if not node.left and not node.right:
		
			if depth not in depths:
				depths.append(depth)
			
			if len(depths) > 2 or (len(depths)==2 and abs(depths[0] - depths[1]) > 1 ):
				
				return False
				
		else:
		
			if node.left:
			
				nodes.append((node.left, depth+1))
			
			if node.right:
			
				nodes.append((node.right, depth+1))
				
	return True
	

print(depth_check(tree))
	
		
