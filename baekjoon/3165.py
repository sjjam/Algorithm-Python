# 5
# r1 x
# https://www.acmicpc.net/problem/3165

# n, k = map(int, input().split())
# end = 10**15
# now = list(map(int, str(n + 1)))
# idx = len(now) - 1

# while True:
#     if now.count(5) >= k:
#         break
#     if idx < 0:
#         now.insert(0, 1)
#         idx = 0

#     if now[idx] != 5:
#         if now[idx] > 5:
#             if idx - 1 < 0:
#                 now[idx] = 5
#                 now.insert(0, 1)
#                 idx = len(now) - 1
#                 continue
#             plus = idx - 1
#             while now[plus] == 9:
#                 now[plus] = 0
#                 plus -= 1
#                 if plus < 0:
#                     now.insert(0, 1)
#                     idx = len(now) - 1
#                     break
#             if plus >= 0:
#                 now[plus] += 1
#         now[idx] = 5
#     idx -= 1

# print(int(''.join(list(map(str, now)))))




# https://welog.tistory.com/296

N, K = map(int, input().split())
N += 1
N_list = list(str(N))
cur_idx = -1
max_idx = len(N_list)
while True:
    if N_list.count('5') >= K:
        break
    while N_list[cur_idx] == '5' and abs(cur_idx) < max_idx:
        cur_idx -= 1
    
    cur_value = int(''.join(N_list))
    cur_value = cur_value + 10**(abs(cur_idx)-1)
    N_list = list(str(cur_value))
    max_idx = len(N_list)

print(''.join(N_list))