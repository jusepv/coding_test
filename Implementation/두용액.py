N = int(input())

ls = list(map(int, input().split()))
# ls = [-2, 4, -99, -1, 98]


ls.sort()

min_sum = float('inf')
left, right = 0, N-1

result = [0, 0]

while left < right:
    current_sum = ls[left] + ls[right]
    # 
    if abs(current_sum) < min_sum:
        min_sum = abs(current_sum)
        result = [ls[left], ls[right]]

    if current_sum > 0:
        right -= 1
    elif current_sum < 0:
        left += 1
    else:
        break

print(*result)