class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        ans =[]
        carry =0
        i = 0
        j = 0
        while i < len(a) or j < len(b) or carry >0:
            if i < len(a):
                bit_a = int(a[i])
            else:
                bit_a = 0
            if j < len(b):
                bit_b = int(b[j])
            else:
                bit_b = 0
            total = bit_a + bit_b + carry
            ans.append(str(total%2))
            carry = total//2
            i+= 1
            j+= 1
        return "".join(ans[::-1])