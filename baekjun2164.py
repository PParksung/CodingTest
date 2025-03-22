from collections import deque

n = int(input())
q = deque(range(1, n+1))

while len(q) > 1:
    q.popleft()         # 1. 제일 위 카드 버림
    q.append(q.popleft())  # 2. 다음 카드를 맨 뒤로

print(q[0])
