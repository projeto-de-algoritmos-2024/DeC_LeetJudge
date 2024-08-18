from questao493 import Solution
import unittest

class TestReversePairs(unittest.TestCase):
    def test_exemple_1(self):
        s = Solution()
        saida = s.reversePairs([1,3,2,3,1])
        esperado = 2
        self.assertEqual(saida, esperado)
    
    def test_exemple_2(self):
        s = Solution()
        saida = s.reversePairs([2,4,3,5,1])
        esperado = 3
        self.assertEqual(saida, esperado)


if __name__ == '__main__':
    unittest.main()