class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_and_count(nums, indices, temp_indices, left, mid, right):
            i = left
            j = mid + 1
            count = 0
            temp_idx = left

            while i <= mid and j <= right:
                if nums[indices[i]] <= nums[indices[j]]:
                    temp_indices[temp_idx] = indices[i]
                    counts[indices[i]] += j - (mid + 1)
                    i += 1
                else:
                    temp_indices[temp_idx] = indices[j]
                    j += 1
                temp_idx += 1

            while i <= mid:
                temp_indices[temp_idx] = indices[i]
                counts[indices[i]] += j - (mid + 1)
                i += 1
                temp_idx += 1

            while j <= right:
                temp_indices[temp_idx] = indices[j]
                j += 1
                temp_idx += 1

            for i in range(left, right + 1):
                indices[i] = temp_indices[i]

            return count
        
        def sort_and_count(nums, indices, temp_indices, left, right):
            count = 0
            if left < right:
                mid = (left + right) // 2
                
                count += sort_and_count(nums, indices, temp_indices, left, mid)
                count += sort_and_count(nums, indices, temp_indices, mid + 1, right)
                count += merge_and_count(nums, indices, temp_indices, left, mid, right)
                
            return count

        n = len(nums)
        indices = list(range(n))
        temp_indices = [0] * n
        global counts
        counts = [0] * n
        
        sort_and_count(nums, indices, temp_indices, 0, n - 1)
        
        return counts
