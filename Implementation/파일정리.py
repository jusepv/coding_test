import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())

ext_count = defaultdict(int)

for _ in range(N):
    ext = sys.stdin.readline().strip().split('.')[-1]
    ext_count[ext] += 1

for ext in sorted(ext_count.keys()):
    print(ext, ext_count[ext])