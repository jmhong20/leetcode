class Solution:
    def checkRecord(self, s: str) -> bool:
        absents = 0
        lates = 0

        for attendance in s:
            if attendance == 'A':
                absents += 1
            if attendance == 'L':
                lates += 1
            else:
                if lates > 0 and lates < 3:
                    lates = 0
        
        return absents < 2 and lates < 3
