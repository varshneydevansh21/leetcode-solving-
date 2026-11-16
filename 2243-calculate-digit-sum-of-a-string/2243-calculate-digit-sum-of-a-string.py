class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) == k:
            return s
        while len(s) > k:
            temp = ""
            for i  in range(0,len(s),k):
                grp = s[i:i+k]
                total = sum(int(digit) for digit in grp)
                temp += str(total)
            s = temp 
        return s