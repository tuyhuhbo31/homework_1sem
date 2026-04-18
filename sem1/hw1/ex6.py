s = list(map(int, input().split()))
for i in range(len(s)):
    if s.count(s[i]) == 1:
        print(s[i], end=" ")