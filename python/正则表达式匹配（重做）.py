class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        def matches(i, j):#ij表示第几个字符是否匹配
#如果i,j=1,1，实际上匹配的就是两个字符串的第1个字符，即s[0],p[0]
            if i == 0:
                return False
            if p[j - 1] == '.':#是点的话一定匹配
                return True
            return s[i - 1] == p[j - 1]
#f的数字表示当前的进度，f[3][2]表示s前3个字符与p前2个字符是否匹配
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':#若当前p字符是星号
                    f[i][j] = f[i][j - 2]#星号重复0次，则去掉两个字符
                    if matches(i, j - 1):
            #说明星号前字符与当前s字符匹配，结果取决于前面
#为什么是f[i-1][j]，看前面的话，i-1不难理解，取j是因为j是星号，包含了所有可能性
                        f[i][j] |= f[i - 1][j]#这里需要用|，是因为前面考虑了重复0次的情况已经填了一次f[i][j]，这里是再考率重复n次的情况，只要其中有一次是真即可
                #因为即使i与j-1字符是一致的，也不代表一定要进行一次匹配
                else:
                    if matches(i, j):
    #若返回True则说明ij必然匹配，则结果取决于前面是否匹配
                        f[i][j] = f[i - 1][j - 1]
        return f[m][n]
