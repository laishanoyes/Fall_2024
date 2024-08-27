import math

def find_inverse(num1, num2):
	t, newt = 0, 1
	r, newr = num2, num1

	while newr != 0:
		quotient = r // newr
		t, newt = newt, t - quotient * newt
		r, newr = newr, r - quotient * newr
	if r > 1:
		return("num1 is not invertible")
	if t < 0:
		t += num2 
	return t



def main():
	num1 = int(input("Please enter the first number: "))
	num2 = int(input("Please enter the second number: "))

	result = find_inverse(num1, num2)
	print(result)

if __name__ == "__main__":
	main()

