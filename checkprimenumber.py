check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate via the check_prime list

for num in check_prime:
    if num == 2:
        print("{} IS a prime number".format(num))
        continue

for i in range(2, num):

    if (num % i) == 0:
        print("{} is NOt a prime number, because {} is a factor of {}".format(num, i, num))
        break

    if i == num -1:
        print("{} IS a prime number".format(num))
        