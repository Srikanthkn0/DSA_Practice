class MedianFinder:

    def __init__(self):
        self.res =[]
        

    def addNum(self, num: int) -> None:
        self.res.append(num)
        

    def findMedian(self) -> float:
        self.res.sort()
        n = len(self.res)

        return self.res[n // 2] if (n & 1) else (self.res[n//2] + self.res[n//2 - 1]) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()