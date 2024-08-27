def to_base_10(text, alphabet):
	power = len(text) - 1
	base10_num = 0
	for symbol in text:
		value = alphabet.index(symbol)
		base10_num += value * (len(alphabet) ** (power))
		power -= 1
	return base10_num
		


def from_base_10(number, alphabet):
	base = len(alphabet)
	message = ""
	while number > 0:
		remainder = number % base
		message = alphabet[remainder] + message
		number //= base
	return message



def main():
	text = "helloworld" 
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	number = 38933758647189
	print(int(to_base_10(text, alphabet)))
	print(str(from_base_10(number, alphabet)))
if __name__ == "__main__":
	main()

