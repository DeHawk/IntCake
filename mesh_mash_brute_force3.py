
# class GraphNode:

	# def __init__(self, label)
	
		# self.label = label
		# self.neighbors = set()
		# self.color = None
		

# a = GraphNode('a')
# b = GraphNode('b')
# c = GraphNode('c')

# a.neighbors.add(b)
# b.neighbors.add(a)
# b.neighbors.add(c)
# c.neighbors.add(b)

# graph = [a, b, c]

graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }
		
from collections import deque

def reconstruct_path(path_dict, start, end):

	shortest_path = []
	current = end	
	
	while current:
		shortest_path.append(current)
		current = path_dict[current]
		
	shortest_path.reverse()
	return shortest_path
	

def mesh_mash(graph, start_node, end_node):

	if start_node not in graph:
		raise Exception('Start node not in graph')
	if end_node not in graph:
		raise Exception('End node not in graph')

	nodes_to_visit = deque()
	
	nodes_to_visit.append(start_node)
	
	#nodes_already_seen = set([start_node])
	
	how_we_reached = {start_node:None}
	
	while nodes_to_visit:
	
		current = nodes_to_visit.popleft()
		
		if current == end_node:
			return reconstruct_path(how_we_reached, start_node, end_node)			
			
		for neighbor in graph[current]:
			if neighbor not in how_we_reached:
				#nodes_already_seen.add(neighbor)
				nodes_to_visit.append(neighbor)
				how_we_reached[neighbor] = current
				

print(mesh_mash(graph, 'a', 'e'))