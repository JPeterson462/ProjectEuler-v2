cap = 20

for n in range(1, 100_000_000):
	valid = True
	for i in range(1, cap+1):
		valid = valid and n % i == 0
		if not valid:
			break
	if valid:
		print(n)