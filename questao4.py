class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        i = j = 0
        numsOrdenados= []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <=  nums2[j]:
                numsOrdenados.append(nums1[i])
                i += 1
            else:
                numsOrdenados.append(nums2[j])
                j += 1

        numsOrdenados += nums1[i:]
        numsOrdenados += nums2[j:]

        n = len(numsOrdenados)
        return (numsOrdenados[n//2]+numsOrdenados[(n//2)-1])/2.0 if n%2==0 else numsOrdenados[n//2]