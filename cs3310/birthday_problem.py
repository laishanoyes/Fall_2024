def main():
	n = 40
	p = 1.0
	for i in range(n):
		p *= (365-i)/365
	p_teacher_wins = 1-p
	print(p_teacher_wins)

main()
