def convert_to_large_base_num(number, base):
	strings = "0123456789ABCDEFGHIJ"
	result = ""
	while number > 0:
		digit = number % base
		result = strings[digit] + result
		number = number // base
	return print(result)

if __name__ == "__main__":
	convert_to_large_base_num(22, 12)