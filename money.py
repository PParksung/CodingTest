def solution(n, money):
    dp = [0]*(n+1)
    dp[0] = 1
    for coin in money: # 1 2 5 하나씩 넣어봄
        for i in range(coin, n+1):
            dp[i] += dp[i - coin]
    return dp[n]

input = list(map(int, input().split()))
n = input[0]
money = input[1:]

print(solution(n, money))