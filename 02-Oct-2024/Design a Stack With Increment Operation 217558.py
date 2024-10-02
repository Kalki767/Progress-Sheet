# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.capacity = maxSize

    def push(self, x: int) -> None:
        if self.capacity > 0:
            self.stack.append(x)
            self.capacity -= 1

    def pop(self) -> int:
        if self.stack:
            res = self.stack.pop()
            self.capacity += 1
            return res
        return -1

    def increment(self, k: int, val: int) -> None:
        cur = min(k,len(self.stack))
        for i in range(cur):
            self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)