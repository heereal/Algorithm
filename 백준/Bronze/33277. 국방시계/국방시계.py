n, m = map(int, input().split())
total_minutes = (m / n) * 24 * 60
hour = int(total_minutes // 60)
minute = int(total_minutes % 60)
print(f'{hour:02d}:{minute:02d}')