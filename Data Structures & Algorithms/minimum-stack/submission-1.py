import heapq
class MinStack:
    
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        heapq.heappush(self.mins, val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins = self.stack[:]
        heapq.heapify(self.mins)
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return heapq.heappop(self.mins)
        
