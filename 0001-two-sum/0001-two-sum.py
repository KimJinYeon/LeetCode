class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = dict()
        for index in range(len(nums)):
            value = nums[index]
            if target - value in value_index:
                return sorted([index, value_index.get(target - value)])
            value_index[value] = index