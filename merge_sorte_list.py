my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

def merge_list(my_list, alices_list):

	my_index, alices_index = 0,0
	my_len, alices_len = len(my_list), len(alices_list)
	
	
	
	merged_list = []
	
	while len(merged_list) < my_len + alices_len:
	
		if my_index < my_len and (alices_index == alices_len or my_list[my_index] <= alices_list[alices_index]):
			merged_list.append(my_list[my_index])
			my_index += 1
			
		else:
			merged_list.append(alices_list[alices_index])
			alices_index += 1
			
	return merged_list
	

print(merge_list(my_list,alices_list))
	