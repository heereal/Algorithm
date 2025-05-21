n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

ns.sort()

def binary_search(low, high, target):
    if low > high:
        return 0

    mid = (low + high) // 2

    if ns[mid] == target:
        return 1
    elif ns[mid] > target:
        high = mid-1
        return binary_search(low, high, target)
    elif ns[mid] < target:
        low = mid+1
        return binary_search(low, high, target)

for num in ms:
    print(binary_search(0, n-1, num))