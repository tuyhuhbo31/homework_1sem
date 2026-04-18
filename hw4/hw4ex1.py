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
    def test_1(self):
        self.assertEqual(func(2), [2])
    def test_2(self):
        self.assertEqual(func(6), [2, 3])
        self.assertEqual(func(12), [2, 2, 3])
    def test_3(self):
        self.assertEqual(func(97), [97])
    def test_4(self):
        self.assertEqual(func(1000000), [2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5])
        
if __name__ == "__main__":
    unittest.main()