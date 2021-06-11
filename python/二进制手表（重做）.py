#小时0-11,亮灯数0-3,  1,2,4,8
#分钟0-59，亮灯数0-5  32,16,8,4,2,1
#rjust(width,fillchar),优先往右边放，然后填充放在左边

#暴力法，创建所有可能情况，人工筛选
from itertools import combinations
class Solution(object):
    def readBinaryWatch(self, num):
        hour = {}
        hour[1] = [1, 2, 4, 8]
        hour[2] = [3, 5, 9, 6, 10]
        hour[3] = [7, 11]
        hour[0] = [0]
        minute = {}
        minute[1] = [1, 2, 4, 8, 16, 32]
        minute[2] = [3, 5, 9, 17, 33, 6, 10, 18,34, 12,20, 36, 24, 40, 48]
        minute[3] = [7, 11, 19, 35, 13,21,37,25,41, 49, 14,22,38,26,42,50,28,44,56,52]
        minute[4] = [15,23,39,27,29,30,43,45,46,51,53,54,57,58]
        minute[5] = [31, 47, 55, 59]
        minute[0] = [0]
        res = []
        for i in range(num+1):#i是小时的亮灯数，j是分钟的亮灯数
            j = num - i
            if i in hour and j in minute:#首先亮灯数不能超过上限
                for hh in hour[i]:
                    for mm in minute[j]:
                        res.append(str(hh) + ':' + str(mm).rjust(2,'0'))
        return res
#不用人工筛选，通过函数排除掉不可能的
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def possible_number(count, minute=False):#count表示亮灯数
            if count == 0: return [0]
            if minute:
                return filter(lambda a: a < 60, map(sum, combinations([1, 2, 4, 8, 16, 32], count)))
#combinations函数作用为对列表进行长度为count的排列组合，combinations([1,2,3],2)->(1,2),(1,3),(2,3),注意，最终返回的是一个可迭代参数
            return filter(lambda a: a < 12, map(sum, combinations([1, 2, 4, 8], count)))
        ans = set()
        for i in range(min(4, num + 1)):#小时亮灯数最高为3
            for a in possible_number(i):
                for b in possible_number(num - i, True):
                    ans.add(str(a) + ":" + str(b).rjust(2, '0'))
        return list(ans)


