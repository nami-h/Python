import itertools 

word, n = input().split()
for i in range(1, int(n)+1):
    [print("".join(i)) for i in itertools.combinations(sorted(word), i)]
