N = 7755

half_idx = len(str(N)) // 2

left = str(N)[:half_idx]
right = str(N)[half_idx:]

left_ls = [int(i) for i in left]
right_ls = [int(i) for i in right]

if sum(left_ls) == sum(right_ls):
    print('LUCKY')
else:
    print('READY')
