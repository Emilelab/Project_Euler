#2520 is the smallest number that can be divided by each of the numbers from 
#1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 
#1 to 20?

"""Brute Force, very long, very stupid
for i in range (1, 10000000000000):
    for j in range (1, 21):
        print("Testing:",i)
        a = i%j
        if a == 0 and j == 20:
            print("The answer is:",i)
            exit()
        elif a == 0:
            continue
        else:
            break"""


