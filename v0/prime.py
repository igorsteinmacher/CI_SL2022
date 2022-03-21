def is_prime(number): 	
	if (not type(number) is int):
		return False
	if (number <= 1):
		return False
	for element in range(2,number): 
		if (number % element == 0):
			return False
	return True 
