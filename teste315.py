from questao315 import Solution  
import unittest

class TestCountSmaller(unittest.TestCase):
    def test_exemplo_1(self):
        s = Solution()
        saida = s.countSmaller([5, 2, 6, 1])
        esperado = [2, 1, 1, 0]
        self.assertEqual(saida, esperado)

    def test_exemplo_2(self):
        s = Solution()
        saida = s.countSmaller([1, 1, 1, 1])
        esperado = [0, 0, 0, 0]
        self.assertEqual(saida, esperado)

if __name__ == '__main__':
    unittest.main()
