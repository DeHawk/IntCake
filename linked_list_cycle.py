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

n1 = LinkedListNode('A')
n2 = LinkedListNode('B')
n3 = LinkedListNode('C')
n4 = LinkedListNode('A')
n5 = LinkedListNode('B')
n6 = LinkedListNode('C')
n7 = LinkedListNode('D')

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n3

# def print_linked_list(head):

	# current = head
	# while current.next:
		# print(current.value, "-->")
		# current = current.next
	# print(current.value)
	
# print_linked_list(a)

def check_cycle(head_node):

	faster, slower = head_node, head_node
	slow_trigger = 0
	
	while faster.next:
		faster = faster.next
		if slow_trigger%2 == 1:
			slower = slower.next			
		if faster == slower:
			return True
		slow_trigger += 1
	return False
	

				
print(check_cycle(a))
print(check_cycle(n1))
	


			
	
		
			
		

