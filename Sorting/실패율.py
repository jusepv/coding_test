N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

fail_rate = []


print(stages.count(2))
    
# for n in range(1, N+1):
#     s_total = 0
#     s_success = 0
#     for s in stages:
#         if s >= n:
#             s_total += 1
#         if s > n:
#             s_success += 1
#     fail_rate.append((n, 1-s_success/s_total))
        

# # fail_rate = fail_rate[1:]\
    

# sorted_fail = sorted(fail_rate, reverse=True, key=lambda k: k[1])
# answer = []
# for s in sorted_fail:
#     answer.append(s[0])


# print(answer)