t = int(input())

for _ in range(t):
    sequence = "".join(input().split()[1:])
    arr = sorted(sequence.split("O"), reverse=True)
    longest = len(arr[0])
    print(f'The longest contiguous subsequence of X\'s is of length {longest}')