class Solution:
    def findDelayedArrivalTime(self, a: int, b: int) -> int:
        return (a + b) % 24
        