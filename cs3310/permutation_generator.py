#initialize the list of numbers of length n, starting at zero and going until n-1
def make_nums(n):
	nums = []
	for i in range(n):
		nums.append(i)
	return nums

def next_permutations(nums):
	# make i equal to the second to last index
	i = len(nums) - 2
	#finds the next one that is smaller than its neighbor
	while i >= 0 and nums[i] >= nums [i + 1]:
		i -= 1
	#there are no elements on the right, aka, there are no permutations left
	if i == -1:
		return None
	#finds next smallest besides nums[i]
	j = len(nums) - 1
	while nums[j] <= nums[i]:
		j -= 1
	#swaps i and j
	nums[i], nums[j] = nums[j], nums[i]
	nums[i+1:] = reversed(nums[i + 1:]) 
	#reverses everything on the end to put it in order
	return nums

#print each permutation
def make_perms(nums):
	permutations = []
	while nums:
		permutations.append(nums.copy())
		nums = next_permutations(nums)

	return permutations
		#returns nums as the next permutation

def main(): 
	while True:
		n = int(input("Please enter a number 1-9:"))
		if 1 <= n <= 10:
			break

		else:
			print("Invalid entry, please enter a number between 1 and 9: ")
	nums = make_nums(n)
	make_perms(nums)

if __name__ == "__main__":
	main()
