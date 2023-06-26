from heapq import *

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cost_total = 0
        
        # 뽑아야 하는 직원 수가 전체 직원 수보다 크거나 같으면
        if len(costs) <= k:
            return sum(costs)
        
        # 왼쪽, 오른쪽 heap 겹치는 영역 있는지 확인
        cross = len(costs) <= candidates * 2
        
        # 겹치면 하나로 처리
        if cross:
            heapify(costs)
            for i in range(k):
                cost_total += heappop(costs)
            return cost_total
        # 좌우 나눠서 처리
        else:
            left_wing = costs[:candidates]
            right_wing = costs[-candidates:]
            heapify(left_wing)
            heapify(right_wing)
            costs = costs[candidates:-candidates]
            for i in range(k):
                if left_wing and right_wing:
                    if left_wing[0] <= right_wing[0]:
                        cost_total += heappop(left_wing)
                        if costs:
                            heappush(left_wing, costs.pop(0))
                    else:
                        cost_total += heappop(right_wing)
                        if costs:
                            heappush(right_wing, costs.pop())
                else:
                    if left_wing:
                        cost_total += heappop(left_wing)
                        if costs:
                            heappush(left_wing, costs.pop(0))
                        continue
                    if right_wing:
                        cost_total += heappop(right_wing)
                        if costs:
                            heappush(right_wing, costs.pop())
            return cost_total