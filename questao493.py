class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.contador(nums, 0)[1]

    def contador(self, nums, countInvTotal):
        if len(nums) > 1: 
            meio = len(nums)//2
            # print("-----> ", nums[:meio], nums[meio:])
            numsEsq, countInvEsq = self.contador(nums[:meio], countInvTotal)
            numsDir, countInvDir = self.contador(nums[meio:], countInvTotal)

            numsOrdenados, countInvMerge = self.mergeCount(numsEsq, numsDir)
            countInvTotal += countInvEsq + countInvDir + countInvMerge
            return numsOrdenados, countInvTotal
        else:
            return nums, countInvTotal


    def mergeCount(self, numsEsq, numsDir):
            
            numsOrdenados = []
            countInvMerge = 0

            # Contando os pares reversos
            i = j = 0
            while i < len(numsEsq) and j < len(numsDir):
                if numsEsq[i] > 2 * numsDir[j]:
                    countInvMerge += len(numsEsq) - i
                    j += 1
                else:
                    i += 1

            # Merge das duas partes
            i = j = 0
            while i < len(numsEsq) and j < len(numsDir):
                if numsEsq[i] <= numsDir[j]:
                    numsOrdenados.append(numsEsq[i])
                    i += 1
                else:
                    numsOrdenados.append(numsDir[j])
                    j += 1

            numsOrdenados += numsEsq[i:]
            numsOrdenados += numsDir[j:]

            # print(numsOrdenados, countInvMerge)
            return numsOrdenados, countInvMerge