# def is used to create a function


def calculate_numbers():
	print(10+10)
	print(30+30)


def calculate_numbers_with_params(num1, num2):
	print(num1 + num2)


# with return
def calculate_with_return(n1, n2):
	return n1 * n2


calculate_numbers()
calculate_numbers_with_params(100, 16)

result = calculate_with_return(3, 30)
print(result)
