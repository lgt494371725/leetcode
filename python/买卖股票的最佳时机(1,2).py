class Solution(object):#该方法可用，但复杂度略高
    def maxProfit(self, prices):
        i,j=0,1
        maxprofit=0
        while i <len(prices) and j<len(prices):
            while i <len(prices) and j<len(prices)\
            and prices[i]>=prices[j]:
                i+=1
                j+=1
            if j<len(prices) and (max(prices[j:])-prices[i])>maxprofit:
                maxprofit=max(prices[j:])-prices[i]
            i=j+1
            j=i+1
        return maxprofit
class Solution:#复杂度O（n），稍微好一些
    def maxProfit(self, prices):
        minprice = prices[0]
        maxprofit = 0
        for price in prices:#每天都考虑一次是否卖出
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit

#题目二
class Solution(object):
    def maxProfit(self, prices):
        i,j=0,1
        profit=0
        while i<len(prices) and j<len(prices):
            while i<len(prices) and j<len(prices) and prices[i]>=prices[j]:
                i+=1
                j+=1
            while j<len(prices)-1 and prices[j]<prices[j+1]:#这里注意j是小于长度减1，因为访问了j+1
                j+=1
            if j<len(prices):#使用这种循环要仔细考虑越界问题
                #没有这个if就一定会越界，比如一个递减数组
                profit+=prices[j]-prices[i]
            i=j+1
            j=i+1
        return profit
#更简便的写法，复杂度稍高于第一种
class Solution(object):
    def maxProfit(self, prices):
        profit=0
        for i in range(1,len(prices)):
            profit+=max(0,prices[i]-prices[i-1])
        return profit
