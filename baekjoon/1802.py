# 종이 접기
# https://www.acmicpc.net/problem/1802

# 가운데를 기준으로 대칭(왼쪽이 out이면 오른쪽은 in이어야 겹쳐진다 = 대칭)

for _ in range(int(input())):
    data = list(map(int, input()))
    ans = 'YES'

    while len(data) > 1:
        mid = len(data) // 2
        left = list(data[:mid])
        right = list(data[mid + 1:])
        for i in range(len(left)):
            if left[i] + right[len(left) - 1 - i] != 1:
                ans = 'NO'
                break
        if ans == 'NO':
            break

        if data[mid] == 0:
            data = right
        else:
            data = left
    print(ans)