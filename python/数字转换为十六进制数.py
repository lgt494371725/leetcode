class Solution:
    def toHex(self, num):
        num &= 0xFFFFFFFF
#无论是正数负数，相与之后值都不变，意图在于变成32位的二进制
#负数的话，输入时就会以补码形式保存，无需多考虑，直接转换即可
        s = "0123456789abcdef"
        res = ""
        mask = 0b1111#二进制四位掩码，每次进行四位即1个十六进制的转换
        while num > 0:
            res += s[num & mask]
            num >>= 4
        return res[::-1] if res else "0"
