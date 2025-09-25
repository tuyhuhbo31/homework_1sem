s = list(map(int, input().split()))
a = 0
b = 0
for i in range(len(s)):
    for j in range(i+1,len(s)):
            if s[i] >= s[j]:
                a +=1
            else:
                 b+=1
    if a == b:
         print(s[i])
    else:
         a = 0
         b = 0