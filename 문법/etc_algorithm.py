# 기타 알고리즘

# 소수의 판별
# 2보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수

# 어떤한 수 x를 2부터 x-1까지의 모든 수로 나누어 보기 > 나누어 떨어지는 수가 하나라도 존해하면 x는 소수가 아니다
# 시간 복잡도 O(x) > 비효율적
'''
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))
'''
# 약수 이용 > 제곱근까지 확인
# 시간 복잡도 O(X1/2승)
'''
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))
'''

# 에라토스테네스의 체
# 여러 개의 수가 소수인지 아닌지를 판별할 때 사용
# N보다 작거나 같은 모든 소수를 찾을 때 사용
# 시간 복잡도 O(NlogN)

# 1. 2부터 N까지의 모든 자연수를 나열
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다
# 3. 남은 수 중에서 i의 배수를 모두 제거(i는 제거하지 않는다)
# 4. 더 이싱 반복할 수 없을 때까지 2~3번 반복
'''
import math

n = 1000
array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')
'''

# 투 포인터
# 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘
# 2개의 변수를 이용해 리스트 상의 위치를 기록

# 특정한 합을 가지는 부분 연속 수열 찾기 문제
# 부분 연속 수열의 시작점과 끝점의 위치를 기록

# 1. 시작점과 끝점이 첫 번째 원소의 인덱스(0)를 가리키도록 한다
# 2. 현재 부분합이 M과 같다면 카운트
# 3. 현재 부분합이 M보다 작으면 end를 1 증가
# 4. 현재 부분합이 M보다 크거나 같으면 start를 1 증가
# 5. 모든 경우를 확인할 때까지 2~4번 반복
'''
n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

# start를 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
'''
# 정렬되어 있는 두 리스트의 합집합 같은 문제에 효과적으로 사용
# 두 리스트의 모든 원소를 합쳐서 정렬한 결과를 계산 > 병합 정렬(Merge Sort)과 같은 알고리즘에서 사용
# 2개의 리스트 A, B가 주어졌을 때, 2개의 포인터를 이용해 각 리스트에서 처리되지 않은 원소 중 가장 작은 원소를 가리키면 된다

# 1. 정렬된 리스트 A와 B를 입력받는다
# 2. 리스트 A에서 처리되지 않은 원소 중 가장 작은 원소를 i가 가리키도록 한다
# 3. 리스트 B에서 처리되지 않은 원소 중 가장 작은 원소를 j가 가리키도록 한다
# 4. A[i]와 B[j] 중에서 더 작은 원소를 결과 리스트에 담는다
# 5. 리스트 A와 B에서 더 이상 처리할 원소가 없을 때까지 2~4번 반복
'''
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

result = [0] * (n + m)
i = 0
j = 0
k = 0

while i < n or j < m:
    # 리스트 B의 모든 원소가 처리되었거나, 리스트 A의 원소가 더 작을 때
    if j >= m or (i < n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    # 리스트 A의 모든 원소가 처리되었거나, 리스트 B의 원소가 더 작을 때
    else:
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end=' ')
'''

# 구간 합 계산
# 연속적으로 나열된 N개의 수가 있을 때, 특정 구간의 모든 수를 합한 값을 구하는 문제
# 구간 합 계산 문제는 여러 개의 쿼리로 구성되는 문제 형태로 출제되는 경우가 많다
# 나열된 N개, 쿼리 M개 > 시간 복잡도 O(NM)
# 여러 번 사용될 만한 정보는 미리 구해 저장해 놓을수록 유리하다

# 접두사 합(Prefix Sum)
# N개의 수의 위치 각각에 대하여 접두사 합을 미리 구해 놓는다
# 접두사 합 > 리스트의 맨 앞부터 특정 위치까지의 합을 구해 놓은 것
# 전체 구간 합을 모두 계산하는 작업 > 시간 복잡도 O(N + M)

# 1. N개의 수에 대하여 접두사 합을 계산하여 배열 P에 저장
# 2. 매 M개의 쿼리 정보 [L, R]을 확인할 때, 구간 합은 P[R] - P[L - 1]이다
'''
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
'''

# 순열과 조합
# 파이썬은 순열과 조합 라이브러리를 기본적으로 제공
# 순열과 조합은 재귀 함수 혹은 반복분을 이용해 직접 구현할 수 있다
# itertools 라이브러리 이용

# 경우의 수: 한 번의 시행에서 일어날 수 있는 사건의 가지 수

# 순열
# 서로 다른 n개에서 r개를 선택하여 일렬로 나열
'''
import itertools

data = [1, 2]

for x in itertools.permutations(data, 2):
    print(list(x))
'''
# 조합
# 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택
'''
import itertools

data = [1, 2, 3]

for x in itertools.combinations(data, 2):
    print(list(x), end=' ')
'''
