from questao4 import Solution
import unittest

class TestFindMedianSortedArrays(unittest.TestCase):
    def test_exemple_1(self):
        s = Solution()
        saida = s.findMedianSortedArrays([1,3],[2])
        esperado = 2.00000
        self.assertEqual(saida, esperado)
    
    def test_exemple_2(self):
        s = Solution()
        saida = s.findMedianSortedArrays([1,2],[3,4])
        esperado = 2.50000
        self.assertEqual(saida, esperado)


if __name__ == '__main__':
    unittest.main()