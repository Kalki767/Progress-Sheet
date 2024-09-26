# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
       self.queue = []
       self.size = 0
       self.max_capacity = k
       self.start = 0

    def insertFront(self, value: int) -> bool:
        if self.size < self.max_capacity:
            self.queue.append(value)
            self.size += 1
            for i in range(len(self.queue)-1,self.start,-1):
                self.queue[i], self.queue[i-1] = self.queue[i-1],self.queue[i]
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.max_capacity:
            self.queue.append(value)
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.start < len(self.queue):
            self.start += 1
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.start < len(self.queue):
            self.queue.pop()
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.start < len(self.queue):
            return self.queue[self.start]
        return -1

    def getRear(self) -> int:
        if self.start < len(self.queue):
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.queue) == self.start

    def isFull(self) -> bool:
        return self.size == self.max_capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()