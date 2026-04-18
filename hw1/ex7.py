s = list(map(int, input().split()))
a = 0
for i in range(len(s)):
    if s.count(s[i]) >= a:
        a = s.count(s[i])
for i in range(len(s)):
    if s.count(s[i]) == a:
        print(s[i])
        break