class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        n = len(bills)
        fives, tens = 0,0
        for i in range(0,n):
            if bills[i] == 5:
                fives +=1
            elif bills[i] == 10:
                if fives >=1:
                    fives -=1
                    tens +=1
                else:
                    return False
            else:
                if fives >= 1 and tens >= 1:
                    fives -= 1
                    tens -= 1
                elif fives >=3:
                    fives -= 3
                else: 
                    return False
        return True