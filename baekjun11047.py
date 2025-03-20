number = list(map(int, input().split()))
n, k = number[0], number[1]
coins = []
for _ in range (n):
    num = int(input())
    coins.append(num)

coins.sort(reverse=True)

count = 0
for coin in coins:
    count += k//coin
    k %= coin

print(count)
