#This program calculates the probability of someone winning craps
import random

def RollDice():
	return random.randint(1,6) + random.randint(1,6)


def PlayCraps():
	point = RollDice()
	if point == 7 or point == 11:
		return 1
	if point == 2 or point == 3 or point == 12:
		return 0
	while True:
		x = RollDice()
		if x == point:
			return 1
		if x == 7:
			return 0


def main():
	wins = 0
	TRIES = 1000000
	for i in range (TRIES):
		wins += PlayCraps()
	print("Chances of winning are",wins / TRIES)

main()


