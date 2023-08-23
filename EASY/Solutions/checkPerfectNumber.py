class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sumOfDivs = 0
        div = 1
        
        for i in range(1, num // 2):
            if i * i > num:
                break
            if num % i == 0: 
                sumOfDivs += i
                if i != 1:
                    sumOfDivs += num // i

        return sumOfDivs == num
