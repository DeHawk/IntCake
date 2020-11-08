#liked list


class LinkedListNode(object):

	def __init__(self,value):
		self.value = value
		self.next = None
		

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')


a.next = b
b.next = c
c.next = d

def print_linked_list(head):

	current = head
	while current.next:
		print(current.value, "-->")
		current = current.next
	print(current.value)
	
print_linked_list(a)

def delete_current_node(current_node):

	if current_node.next:
		current_node.value = current_node.next.value
		current_node.next = current_node.next.next
	else:
		current_node.next = None
	
	
	
delete_current_node(b)

print_linked_list(a)
	


			
	
		
			
		

