n = int(input())

array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return binary_search(array, target, start, mid-1)
        else:
            return binary_search(array, target, mid+1, end)
        
for i in x:
    res = binary_search(array, i, 0, n-1)
    if res != None:
        print('yes', end= ' ')
    else:
        print('no', end= ' ')