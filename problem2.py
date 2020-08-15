a = 1
b = 1

total = 0

while a < 4_000_000:
	if b % 2 == 0:
		total += b
	c = a + b
	a = b
	b = c

print(total)