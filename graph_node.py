#create a graph node

# 3 properties - label, neighbors, color

class GraphNode:

	def __init__(self, label)
	
		self.label = label
		self.neighbors = set()
		self.color = None
		

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]
