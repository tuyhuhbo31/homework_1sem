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
    
def inputtvec():
    n = int(input('Введите количество векторов '))
    vectors = []
    for x in range(n):
        t = str(input(f"введите координаты {x+1} вектора : "))
        vectors += [Vector(t)]
    return vectors

vectors = inputtvec()
print(f"Координата центра масс {Vector.centre(vectors)}")
print(f"Максимальная площадь = {Vector.searchS(vectors)}")
