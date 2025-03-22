n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    weight, value = items[i - 1]
    for kg in range(k + 1):
        if kg < weight:
            dp[i][kg] = dp[i - 1][w]  # 못 넣음
        else:
            dp[i][kg] = max(dp[i - 1][kg], dp[i - 1][kg - weight] + value)

print(dp[n][k])
