class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        totalPoisoned = 0
        lastPoisoned = 0
        for time in timeSeries:
            if time > lastPoisoned:
                totalPoisoned += duration
                lastPoisoned = time + duration
            else:
                totalPoisoned -= (lastPoisoned - time)
                totalPoisoned += duration
                lastPoisoned = time + duration

        return totalPoisoned
