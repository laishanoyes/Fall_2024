import math

def find_gcd(num1, num2):
	if num1 > num2:
		a = num1
		b = num2
	else:
		a = num2
		b = num1
	while b != 0:
		a, b = b, a%b
	return(a)


def main():
	num1 = int(input("Please enter the first number"))
	num2 = int(input("Please enter the second number"))

	gcd = find_gcd(num1, num2)

	

if __name__ == "__main__":
	main()
