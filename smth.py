print(3//2)
s = input()
print(s.find('A'))
def func(x, symb):
    if x == 1:
        print(symb*((n-x)//2+1))
        return
    # то что до рекурсивного вызова
    # вызывается на прямом ходу рекурсии
    print(symb*((n-x)//2+1))
    func(x-2,symb)
    # то что после рекурсивного вызова
    # вызывается на обратном ходу рекурсии
    print(symb*((n-x)//2+1))

n = 7
s = '.'
func(n, s)



#if (3 in a) and not (4 in a): #and not == & ~
#    print(3)
#elif(4 in a):
#    print(4)
#else:
#    print('not 3')