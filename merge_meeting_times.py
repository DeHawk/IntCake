input = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
  
  # 30 mins slot
  # sort by start time
  # 
  
def merge_ranges(input):

	num = len(input)
	
	# sort meetings
	
	def sort_meetings(meetings):
	
		if len(meetings) < 2:
			return meetings
			
		mid = len(meetings)//2
		
		left_range = meetings[:mid]
		right_range = meetings[mid:]
		
		sort_left = sort_meetings(left_range)
		sort_right = sort_meetings(right_range)
		
		sorted_meetings = []
		
		left_index, right_index = 0,0
		
		while len(sorted_meetings) < len(sort_left) + len(sort_right):
		
			if (left_index < len(sort_left) and (right_index == len(sort_right) or sort_left[left_index] <= sort_right[right_index])):
				sorted_meetings.append(sort_left[left_index])
				left_index += 1
				
			else:
				sorted_meetings.append(sort_right[right_index])
				right_index += 1
				
		return sorted_meetings
		
	sorted = sort_meetings(input)
	
	merge_meet = []
	
	prev_start, prev_end = sorted[0]
	
	for i in range(1,len(sorted)):
			
		curr_start, curr_end = sorted[i]
		if curr_start <= prev_end:
			prev_start,prev_end = prev_start, max(curr_end, prev_end)
		else:
			merge_meet.append((prev_start,prev_end))
			prev_start,prev_end = curr_start,curr_end
	merge_meet.append((prev_start,prev_end))
	
	return merge_meet
	

output = merge_ranges(input)

print(output)
	
  

  