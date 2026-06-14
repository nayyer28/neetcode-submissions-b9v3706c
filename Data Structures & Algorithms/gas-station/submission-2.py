class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas  = [ 1 , 2 , 4 , 4] => 10

        # cost = [2 , 2 , 4 , 1] => 9
        
        # gain =  -1 , 0, 0, 3

        # gas =  3 1 1
        # cost = 2 3 2


        total_net = 0
        net = 0
        start = 0
        for i in range(len(gas)):
            net += gas[i] - cost[i]
            total_net += gas[i] - cost[i]
            if net < 0:
                net = 0
                start = i + 1
        
        return start if total_net >= 0 else -1
            