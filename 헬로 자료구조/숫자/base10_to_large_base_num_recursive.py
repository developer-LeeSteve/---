def convert_to_large_base_num_recursive(number ,base):
	string = "0123456789ABCDEFGHIJ"
	if number < base:
		return string[number]
	else:
		return convert_to_large_base_num_recursive(number // base, base) + string[number % base]

if __name__ == "__main__":
	convert_to_large_base_num_recursive(15, 12)