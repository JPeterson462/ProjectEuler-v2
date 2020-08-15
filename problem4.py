from utils import reverse_number, count_digits

maxval = 0

digits = 3
cap = 10 ** digits

for a in range(1, cap):
	if count_digits(a) is not digits:
		continue
	for b in range(1, cap):
		if count_digits(b) is not digits:
			continue
		if reverse_number(a * b) == (a * b):
			maxval = max(maxval, a * b)

print(maxval)