from questao215 import Solution  
import unittest

class TestFindKthLargest(unittest.TestCase):
    def test_exemplo_1(self):
        s = Solution()
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        saida = s.findKthLargest(nums, k)
        esperado = 5
        self.assertEqual(saida, esperado)

    def test_exemplo_2(self):
        s = Solution()
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        saida = s.findKthLargest(nums, k)
        esperado = 4
        self.assertEqual(saida, esperado)

if __name__ == '__main__':
    unittest.main()
