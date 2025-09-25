s = input().split()
c = [(s[i+1]) if i%2 == 0 else (s[i-1]) for i in range(len(s) - len(s)%2)]
print(' '.join(c if len(s)%2 == 0 else c+[s[-1]]))