int_list =   [1, 7, 3, 4]



def get_products_of_all_ints_except_at_index(int_list):

	if len(int_list) < 2:
	
		raise ValueError('cannot perform operation')
		
	ints_before = [None] * len(int_list)
	
	rest_prod = [None] * len(int_list)
	
	product_so_far = 1
	
	for i in range(0,len(int_list)):
	
		ints_before[i] = product_so_far
		product_so_far *= int_list[i]
		
	product_so_far = 1
	
	for i in range(len(int_list)-1, -1, -1):
	
		rest_prod[i] = ints_before[i] * product_so_far
	
		product_so_far *= int_list[i]
		
	return rest_prod
		
	
print(get_products_of_all_ints_except_at_index(int_list))
		
	
	