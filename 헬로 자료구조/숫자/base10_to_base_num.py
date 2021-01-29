def convert_to_base_num(number, base):
	multiplier, result = 1, 0
	while number > 0:
		result += number % base * multiplier
		multiplier *= 10
		number = number // base
	return print(result)

if __name__ == "__main__":
	convert_to_base_num(23, 2)