from collections import deque

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = deque()
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                merged_list.append(nums1.pop(0))
            else:
                merged_list.append(nums2.pop(0))
        else:
            while nums1:
                merged_list.append(nums1.pop(0))
            while nums2:
                merged_list.append(nums2.pop(0))
        print(merged_list)
        
        if len(merged_list) % 2:  # 홀수면
            return merged_list[len(merged_list) // 2]
        else:
            return (merged_list[len(merged_list) // 2] + merged_list[len(merged_list) // 2 - 1]) / 2