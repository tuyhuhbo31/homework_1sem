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