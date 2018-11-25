# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

word, num=input().split()

num=int(num)

for i in itertools.permutations(sorted(word), num):
    print("".join(i))
