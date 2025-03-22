n = int(input())
string = [input() for _ in range (n)]

for list in string:
    if len(list) == 0:
        print(list+list)    
    else:
        first = list[0]
        last = list[-1]
        print(first+last)