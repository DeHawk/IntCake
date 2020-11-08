
def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
	
	movie_set = set()
	
	for mov_len in movie_lengths:
		if mov_len in movie_set:
			return True
		else:
			movie_set.add(flight_length - mov_len)


    return False
	
	

m_lengths = [1, 2, 3, 4, 5, 6]
f_length = 7