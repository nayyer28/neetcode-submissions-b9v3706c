class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = []
        self.hmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hmap:
            return ""
        
        # 10 20 30
        values = self.hmap[key]

        l, r, mid = 0, len(values) - 1, 0

        while l <=r:

            mid = (l+r) // 2

            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                l += 1
            else:
                r -= 1
        

        if timestamp > values[mid][1]: # eg. look for 15 in 10 20 30 --> mid ends at 10
            return values[mid][0]
        elif mid - 1 >=0: # eg. look for 25 or 8 in 10 20 30 
            return values[mid - 1][0]
        else:
            return ""