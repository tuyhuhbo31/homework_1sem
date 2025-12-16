class ThreeDVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return ((self.x)**2 + (self.y)**2 + (self.z)**2)**(1/2)
    def __add__(self, other):
        assert isinstance(other, ThreeDVector), "Операция определена  только для векторов"
        return ThreeDVector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'
    def __sub__(self, other):
        assert isinstance(other, ThreeDVector), "Операция определена  только для векторов"
        return ThreeDVector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        assert (isinstance(other, ThreeDVector) or isinstance(other, int) or isinstance(other, float))
        if isinstance(other, ThreeDVector):
            return (self.x*other.x + self.y*other.y + self.z*other.z)
        if (isinstance(other, int) or isinstance(other, float)):
            return ThreeDVector(self.x*other, self.y*other, self.z*other)
        else:
            raise ValueError(f'Эта операция не определена')
    def __rmul__(self, other):
        assert (isinstance(other, ThreeDVector) or isinstance(other, int) or isinstance(other, float))
        if (isinstance(other, int) or isinstance(other, float)):
            return ThreeDVector(self.x*other, self.y*other, self.z*other)
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


def input_vector():
    input_str = input("Введите координаты вектора (x,y,z): ")
    crds = [float(crds) for crds in input_str.split()]
    if len(crds) != 3:
        print("Ошибка: нужно ввести ровно 3 координаты")
        return None
    return ThreeDVector(crds[0], crds[1], crds[2])
def mass_c(dotlist):
    mc = ThreeDVector(0, 0 ,0)
    for vect in dotlist:
        mc += vect*((N)**(-1))
    return mc

N = int(input('Введите количество точек:'))
dotlist = []
for i in range(N):
    vect = input_vector()
    dotlist.append(vect)
    if vect is None:
        vect = ThreeDVector(0,0,0)
        dotlist.append(vect)
c_mass = mass_c(dotlist)
max_S = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if ((dotlist[i].x/dotlist[j].x) == (dotlist[i].y/dotlist[j].y) == (dotlist[i].z/dotlist[j].z)) and ((dotlist[i].x/dotlist[k].x) == (dotlist[i].y/dotlist[k].y) == (dotlist[i].z/dotlist[k].z)):
                continue
            if i == N-2:
                break
            if j == N-1:
                continue
            s1 = abs(dotlist[j] - dotlist[i])
            s2 = abs(dotlist[k] - dotlist[i])
            s3 = abs(dotlist[k] - dotlist[j])
            pp = (s1 + s2 + s3)/2
            sq = (pp*(pp-s1)*(pp-s2)*(pp-s3))**(0.5)
            if sq > max_S:
                max_S = sq
print(max_S)



def func(n):
    if n == 1:
        return [1]
    
    f = []
    g = 2
    
    while g * g <= n:
        while n % g == 0:
            f.append(d)
            n //= g
        g += 1 if g == 2 else 2 
    
    if n > 1:
        f.append(n)
    
    return f

import unittest

class BaseTest(unittest.TestCase):
    def test_subprimes(self):
        self.assertListEqual(func(2), [2])
        self.assertListEqual(func(3), [3])
    def test_primes(self):
        self.assertListEqual(func(7), [7])
        self.assertListEqual(func(11), [11])
        self.assertListEqual(func(977), [977])
    def test_simple_compounds(self):
        self.assertListEqual(func(6), [2, 3])
        self.assertListEqual(func(8), [2, 2, 2])
        self.assertListEqual(func(121), [11, 11])
        self.assertListEqual(func(2), [2])
    def test_complex_compounds(self):
        self.assertListEqual(func(120120), [2, 2, 2, 3, 5, 7, 11, 13])

if __name__ == "__main__":
    unittest.main()

