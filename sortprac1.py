def bulbble_sort(arr):
    n = len(arr)
    for i in range(n-1): #0,1,2
        for j in range(n-1-i): # 0~2 / 0~1/ 0
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr1 = list(map(int, input().split()))
bulbble_sort(arr1)
print("버블정렬: ", arr1)

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_inx]:
                min_idx = j