import random
import math

def run_Millers_test(p):
	for i in range(20):
		OK = Millers_test(p)
		if not OK:
			return False 
	return True


def Millers_test(p):
	t = p-1
	s = 0
	while t%2 == 0:
		t = t//2
		s +=1
	b = random.randrange(2,p)
	if pow(b,t,p) == 1:
		return True
	for i in range(s):
		if pow(b,t,p) == p-1:
			return True
		t *=2
	return False

def main():

		while True:
			p = int(input("Please enter an odd number to test if it is prime: "))
			if p%2 != 0:
				break

			print("Please enter an ODD number:")
		prime = run_Millers_test(p)
		if prime == True:
			print("Your number is most likely prime")
		else:
			print("Your number is composite.")


if __name__ == "__main__":
	main()
