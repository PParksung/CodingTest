t = int(input())
lines = [input() for _ in range(t)]
result = []

for line in lines:
    stack = []
    is_valid = True
    for c in line:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                is_valid = False
                break
            stack.pop()
    if stack:
        is_valid = False
    
    if is_valid == True:
        answer = "YES"
    else:
        answer = "NO"
    result.append(answer)

for ans in result:
    print(ans)

