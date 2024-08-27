from permutation_generator import *
	#* imports all of the file, not just a specific function

def calculate_wins_and_losses(n_people):
	good = 0
	bad = 0
	total = 0
	list_of_perms = make_nums(n_people)
	possibilities = make_perms(list_of_perms)

	for i in possibilities:
		total += 1
		if all(index != p for index, p in enumerate(i)):
		#enumerate compares a value and its index in a string
			good += 1
		else:
			bad += 1
	return [good, bad, total]




def main():
	while True:
		n_people = int(input("Pick a number between 2 and 10: "))
		if 2 <= n_people <= 10:
			break

		else:
			print("Invalid entry, please choose a number between 2 and 10: ")
	chances = calculate_wins_and_losses(n_people)
	wins = chances[0]
	loss = chances[1]
	tries = chances[2]

	print(f"{wins} of {tries} possible. Probability of a no one getting themselves is", wins/tries)

if __name__ == "__main__":
	main()
