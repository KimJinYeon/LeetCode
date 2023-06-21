class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        left = 1
        right = max(nums)
        
        while abs(right - left) > 1:
            left_third = left + (right - left) / 3
            right_third = right - (right - left) / 3
            
            if self.get_cost(left_third, nums, cost) < self.get_cost(right_third, nums, cost):
                right = right_third
            else:
                left = left_third
        
        return self.get_cost(int(right), nums, cost)
    
    def get_cost(self, target, nums, costs):
        cost_total = 0
        
        for num, cost in zip(nums, costs):
            cost_total += abs(target - num) * cost
            
        return cost_total