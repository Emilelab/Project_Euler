#2520 is the smallest number that can be divided by each of the numbers from 
#1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 
#1 to 20?


for i in range (20, 10000000000000, 20):
    for j in range (20, 10, -1):
        print("Testing:",i)
        a = i%j
        if a == 0 and j == 11:
            print("The answer is:",i)
            exit()
        elif a == 0:
            continue
        else:
            break
"""
Could I still 'brute force' but quicker and smarter?
Don't need to test 1 because every positive int should be divisable by 1
Don't need to test 10 if divisable be 20, etc.
20
19
18
17
16
15
14
13
12
11

nope still dumb... got to 52533567 before shutting it down
"""
