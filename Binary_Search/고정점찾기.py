n = int(input())
array = list(map(int, input().split()))


def binary_search(arr, start, end):
    # while start <= end:
    if start > end:
        return None
    mid = (start+end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        # end = mid - 1
        return binary_search(arr, start, mid-1)
    else:
        # start =  mid + 1 
        return binary_search(arr, mid+1, end)
    
index = binary_search(array, 0, n-1)

if index == None:
    print(-1)
else:
    print(index)