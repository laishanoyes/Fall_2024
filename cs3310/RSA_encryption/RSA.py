import math 
import Millers


class RSA:
	def __init__(self):
		self.alphabet1 = "abcdefghijklmnopqrstuvwxyz"
		self.alphabet2 = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


	def GenerateKeys(self, string1, string2):
		string_p = ''.join(string1.split()).lower()
		string_q = ''.join(string2.split()).lower()
		p = self.to_base10(string_p, self.alphabet1)
		q = self.to_base10(string_q, self.alphabet1)
	
#ensure p and q are long enought
		if len(str(p)) < 200: 
			print("string one is too short")
			return
		if len(str(q)) < 200:
			print("string two is too short")
			return

#ensure p and q are not too long
		p = p % (10 ** 200)
		q = q % (10 ** 200)

#make odd if even
		if p % 2 == 0:
			p += 1
		if q % 2 == 0:
			q += 1

#check prime
		while True:
			if Millers.run_Millers_test(p):
				break
			else:
				p += 2
		while True:
			if Millers.run_Millers_test(q):
				break
			else:
				q += 2

#calculate n and r
		n = p*q
		r = (p-1)*(q-1)
#find e
		e = pow(10, 398) + 1
		while self.find_gcd(e, r) != 1:
			e += 1

#find d using e
		d = self.find_inverse(e, r)
#		print(e*d%r)	

#		print (" P is: ", str(p))
#		print (" Q is: ", str(q))
#		print (" E is: ", str(e))
#		print (" R is: ", str(r))
#		print (" D is: ", str(d))
#		print (" N is: ", str(n))


#write n and e to public.txt
		with open('public.txt', 'w') as f:
			f.write(str(n) + ("\n"))
			f.write(str(e))
#write n and d to private.txt
		with open('private.txt', 'w') as f:
			f.write(str(n) + ("\n"))
			f.write(str(d))
#		x = 1000
#		y = pow(x, e, n)
#		z = pow(y, d, n)
#		print("Z: ", z)


	def Encrypt(self, input_name, output_name):
#read n and e from public.txt
		with open("public.txt", "r") as f:
			n = int(f.readline().strip())
			e = int(f.readline().strip())
#		print("N is: ", str(n))
#		print("E is: ", str(e))

		with open("private.txt", "r") as f:
			n = int(f.readline().strip())
			d = int(f.readline().strip())
#open input as binary and convert to base 10
		with open(input_name, "rb") as fin:
			PlainTextBinary = fin.read()
		PlainText = PlainTextBinary.decode("utf-8")
		print(PlainText)
#divide into blocks 
	#determine number of blocks needed		
		blocks_needed = math.ceil(len(PlainText)/216)
		print(blocks_needed)
		characters_in_block = math.ceil(len(PlainText)/blocks_needed)
		print(characters_in_block)


#convert to base 70
		alphabet2 = self.alphabet2
#encrypt through RSA rules

#Back to base 70
		encoded_blocks=[]
		for i in range(blocks_needed):
			if i == blocks_needed -1:
				plain_text_block = PlainText[i * characters_in_block:]
			else:
				plain_text_block = PlainText[i*characters_in_block:(i+1)*characters_in_block]
		
			plain_block = self.to_base10(plain_text_block, alphabet2)
			encrypt_block = pow(plain_block, e, n)
			encrypt_text_block = self.from_base10(encrypt_block, alphabet2)
			encrypt_text_block += "$"
			encoded_blocks.append(encrypt_text_block)
	
		print("Plain block: ", plain_block)
		print("Encrypted blocks: ", encrypt_block)
		print("back: ", pow(encrypt_block, d, n))

		print("Encrypted_text: ", encrypt_text_block)
		print("Encrypted text with blocks: ", encoded_blocks)
	
		fout = open(output_name, 'wb')
		for block in encoded_blocks:
			fout.write(block.encode("utf-8"))
		fout.close()

#write to output file 
##		with open(output_name, 'wb') as fout:
##			for en in encrypted_blocks:
##				fout.write(en.encode("utf-8"))
##				fout.write(b"$")
##		with open(output_name, 'r') as fin:
##			en_text = fin.read
##		print("Encrypted file: ", en_text)

#write decrypt method 
	def Decrypt(self, input_name, output_name):
		with open(input_name, "rb") as fin:
			encrypted_text_binary = fin.read()
		encrypted_text = encrypted_text_binary.decode("utf-8")
#read n and d from private file
		with open("private.txt", "r") as f:
			n = int(f.readline().strip())
			d = int(f.readline().strip())
# split blocks apart 
		en_blocks = encrypted_text.split("$")
		numbers = [self.to_base10(block, self.alphabet2) for block in en_blocks]
		de_blocks = [pow(number, d, n) for number in numbers]
		decrypted_text = ''.join([self.from_base10(num, self.alphabet2) for num in de_blocks])

#write the decrypted message
		with open(output_name, 'wb') as fout:
			fout.write(''.join(decrypted_text).encode("utf-8"))

		with open(output_name, 'r') as fin:
			de_text = fin.read()
		print(de_text)


#find GCD of two numbers
	def find_gcd(self, num1, num2):
		if num1 > num2:
			a = num1
			b = num2
		else: 
			a = num2
			b = num1
		while b != 0: 
			a, b = b, a%b
		return(a)

#find inverse mod of two numbers
	def find_inverse(self, num1, num2):
		t, newt = 0, 1
		r, newr = num2, num1

		while newr != 0: 
			quotient = r // newr
			t, newt = newt, t - quotient * newt
			r, newr = newr, r - quotient * newr
		if r > 1:
			return("Not invertible")
		if t < 0:
			t += num2
		return t

#convert to base 10
	def to_base10(self, text, alphabet):
		power = len(text) -1
		base10_num = 0
		for symbol in text:
			value = alphabet.index(symbol)
			base10_num += value * (len(alphabet) ** (power))
			power -= 1
		return base10_num

#convert from base 10
	def from_base10(self, number, alphabet):
		base = len(alphabet)
		message = ""
		while number > 0: 
			remainder = number % base
			message = alphabet[remainder] + message
			number //= base
		return message

def main():
#initiate class
	rsa = RSA()

#	string1 = input("Please enter your first string for key generation: ")
#	string2 = input("Please enter your second string for key generation: ")
	string1 = "In a galaxy far far away at a very random point in time nothing was happening this was odd as something should have been happening at that very moment according to jerrys science but jerry is was usually wrong"
	string2 = "Why is jerry usually wrong you may ask well he just guesses and then attempts to prove himself right I mean it worked when he accidentally discovered time travel but it would not work this time not when he was trying to save the world"

	rsa.GenerateKeys(string1, string2)
	
	input_e_file = "input.txt"
	output_e_file = "encrypted.txt"
#	rsa.Encrypt(input_e_file, output_e_file)
	
	input_d_file = "LaishaEncrypted.txt"
	output_d_file = "decrypted_message.txt"
	rsa.Decrypt(input_d_file, output_d_file)





if __name__ == "__main__":
	main()









