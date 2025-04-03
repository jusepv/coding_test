arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# 시계 방향 90도 회전
arr_90 = list(map(list, zip(*arr[::-1])))
print("90도 회전: ", arr_90)

# 시계 방향 
arr_180 = [arr[::-1] for a in arr[::-1]]
print("180도 회전: ", arr_180)