class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def kthLargest(nums, k):
            if len(nums) <= 5:
                return sorted(nums, reverse=True)[k-1]
            
            medians = []
            for i in range(0, len(nums), 5):
                group = sorted(nums[i:i+5])
                median = group[len(group) // 2]
                medians.append(median)
            
            mom = kthLargest(medians, len(medians) // 2 + 1)
            L = [x for x in nums if x > mom]
            R = [x for x in nums if x < mom]
            M = [x for x in nums if x == mom]
            
            if len(L) >= k:
                return kthLargest(L, k)
            elif len(L) + len(M) >= k:
                return mom
            else:
                return kthLargest(R, k - len(L) - len(M))
        
        
        return kthLargest(nums, k)
