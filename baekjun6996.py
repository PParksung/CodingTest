n = int(input())
word = [input().split() for _ in range (n)]

for w1, w2 in word:
    if sorted(w1) == sorted(w2):
        print("%s & %s are anagrams." %(w1, w2))
    else:
        print("%s & %s are NOT anagrams." %(w1, w2))