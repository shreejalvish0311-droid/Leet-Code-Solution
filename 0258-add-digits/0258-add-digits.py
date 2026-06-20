class Solution:
    def addDigits(self, num: int) -> int:
     
        if num < 10:
            return num
            
        def digitSum(n):
            if n == 0:
                return 0
            return n % 10 + digitSum(n // 10)

        return self.addDigits(digitSum(num))