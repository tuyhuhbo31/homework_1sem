A = [0] * int(input())
for i in range(len(A)):
    A[i] = int(input())
b = 1
for i in range(len(A)):
    b *= A[i]
print(b)


