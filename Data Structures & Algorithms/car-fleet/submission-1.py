class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []

        for p,s in sorted(list(zip(position,speed)), key=lambda x: x[0], reverse=True):
            time = (target - p) / s
            if fleets and time <= fleets[-1][0]:
                continue
            fleets.append((time, s))
        
        return len(fleets)
