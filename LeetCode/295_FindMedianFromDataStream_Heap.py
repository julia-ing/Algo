class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        n = len(self.nums)
        self.nums.sort()
        if n % 2 == 0:
            return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2
        else:
            return self.nums[n // 2]
