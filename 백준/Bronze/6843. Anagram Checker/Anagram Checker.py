from collections import Counter

A = "".join(input().split())
B = "".join(input().split())

if Counter(A) == Counter(B):
    print('Is an anagram.')
else:
    print('Is not an anagram.')