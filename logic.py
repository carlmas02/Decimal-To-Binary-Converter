def decimal_to_binary(num):
	output = ''
	while num >0:
		output += str(num%2)
		num //=2
	return output[::-1]

