# ZIp and Enumerate

# Zip using for loop
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

print("Another example of Zip")

Names = ['Sachin', 'Samir', 'Aayush', 'Sushil', 'Aryan', 'Saughat']
Caste = ['Bista', 'Thapa', 'Magar', 'Bist', 'Gurung', 'Chaudhary']
Rollno = [1, 2, 3, 4, 5, 6]

for name, cast, roll in zip(Names, Caste, Rollno):
    print("{} {}: {}".format(name, cast, roll))

print("Another Example of Enum:\n")

some_list = [('a', 1), ('b', 2),('c', 3)]
letters, num = zip(*some_list)

# Enumerate

letters = ['a','b','c','d','e']
for i, letter in enumerate(letters):
    print(i, letter)

Names = ['Sachin Bista', 'Samir Thapa Magar', 'Saughat Chaudhary', 'Aryan Gurung', 'John Rai']
for i, name in enumerate(Names):
    print(i, letter)