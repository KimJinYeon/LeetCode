from collections import deque
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        wing = [-1 for i in range(k)]
        subarray_sum = []
        if len(nums) < 2*k+1:
            return [-1 for i in range(len(nums))]
        for i in range(k, len(nums) - k):
            if subarray_sum:
                subarray_sum.append(subarray_sum[-1] - nums[i-k-1] + nums[i+k])
            else:
                subarray_sum.append(sum(nums[i-k:i+k+1]))
        averages = wing + subarray_sum + wing
        for i in range(len(averages)):
            if averages[i] != -1:
                averages[i] //= 2 * k + 1
        return averages