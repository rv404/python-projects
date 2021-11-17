from math import sqrt

def is_prime(n):
	if n <= 1:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return True
	
	i = 3
	while i <= sqrt(n):
		if n % i == 0:
			return False
		i += 2
		
	return True

def prime_generator():
	n = 1
	while True:
		n += 1
		if is_prime(n):
			yield n