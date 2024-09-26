import os
import time

#Define the student class
class Student:
#initialize the class with all of the items that should be on each line
	def __init__(self, last_name, first_name, ssn, email, age):
		self.last_name = last_name
		self.first_name = first_name
		self.ssn = ssn
		self.email = email
		self.age = age
#Compare ssn 
	def __eq__(self,other):
		if self.ssn == other.ssn:
			return True
		return False
#Make students into a searchable hash/dictionary
	def hash(self):
		return hash(self.ssn)
#Make each student into a string with their information in order
	def __str__(self):
		return f"{self.last_name} {self.first_name} {self.ssn} {self.email} {self.age}"

#Define you bag/container class
class Bag:
#initalize the container with a list of your items
	def __init__(self):
		self.items = []

#Make sure your item exists
	def exists(self,item):
		return item in self.items

#If your item exists add it to the list
	def insert(self, item):
		if not self.exists(item):
			self.items.append(item)
			return True
		return False

#Return how many items are now in that list
	def size(self):
		return len(self.items)


def main():
	bag = Bag()
#Take note of the starting time
	start_time = time.time()
#Mark the file youa re reading
	file_name = "FakeNames.txt"
#Open and read the file
	if os.path.exists(file_name):
		with open(file_name, 'r') as file:
			for line in file:
				parts = line.strip().split()
				#Make sure all of the lines of the file contain the appropriate information
				if len(parts) != 5:
					print("Invalid line format:", line.strip())
					continue

				last_name, first_name, ssn, email, age = parts
				student = Student(last_name, first_name, ssn, email, age)
#Make sure that the item has not already been inserted into the list, if they have print which item it is
				if not bag.insert(student):
					print(f"Duplicate found: {student}")
#if your file can not be opened this will print
	else:
		print("File not found. Please make sure your file is in the same directory")
#Make note of the end tie
	end_time = time.time()
	total_time = end_time - start_time
	print(f"Total students processed: {bag.size()}")
	print(f"Time taken: {total_time:.2f} seconds")

#Call main
if __name__ == "__main__":
	main()

