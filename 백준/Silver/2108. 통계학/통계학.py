import sys
input = sys.stdin.readline

N = int(input())
nums = [] # 중복 포함
dic = {} # 딕셔너리로 개수 카운트

for i in range(N):
    num = int(input())

    nums.append(num)

    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

# 가장 많이 나타나는 값의 개수
max_value = max(dic.values())

# 최빈값 추출
sorted_keys = sorted({k: v for k, v in dic.items() if v >= max_value})

# 최빈값 여러 개일 경우 두 번째로 작은 값 출력
mode = sorted_keys[1] if len(sorted_keys) > 1 else sorted_keys[0] 

print(round(sum(nums)/N)) # 산술평균
print(sorted(nums)[N//2]) # 중앙값
print(mode) # 최빈값
print(max(nums)-min(nums)) # 범위