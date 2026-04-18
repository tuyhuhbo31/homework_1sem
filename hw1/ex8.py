n = int(input())
s = list(map(int, input().split()))
a = 0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i] <= s[j]:
            a = s[i]
            s[i] = s[j]
            s[j] = a
print(s[len(s)//2])