def cal(len):
    if len <= 1:
        return "-"
    return cal(len//3) + " "*(len//3) + cal(len//3)

while True:
    try:
        N = int(input())
        print(cal(3**N))
    except:
        break