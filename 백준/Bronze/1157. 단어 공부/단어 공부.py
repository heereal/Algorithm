word = input().upper()
word_list = list(set(word)) 
cnt = []

for i in word_list:
    cnt.append(word.count(i)) 


max_count = max(cnt)
if cnt.count(max_count) > 1:
    print("?")
else:
    print(word_list[cnt.index(max_count)])