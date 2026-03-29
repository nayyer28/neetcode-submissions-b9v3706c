class TimeMap:

    def __init__(self):
        self.htable = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.htable:
            self.htable[key].append((value, timestamp))
        else:
            self.htable[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.htable:
            return ""
        values = self.htable[key]
        left, right = 0, len(values) - 1
        # 1 3 5 7 9 15
        # key1 -> [(value1, 10)]
        while left <= right:
            mid = (left + right) // 2

            if timestamp == values[mid][1]:
                return values[mid][0]
            
            if timestamp < values[mid][1]:
                right = mid - 1
            else:
                left = mid + 1

        if values[mid][1] <= timestamp:
            return values[mid][0]
        elif mid - 1 >= 0:
            return values[mid - 1][0]
        else:
            return ""
                
        
