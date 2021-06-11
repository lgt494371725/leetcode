#分支结构
# 单分支 if xx==xx
#二分支
guess=eval(input())
if guess==99:
    print("猜对了")
else:
    print("猜错了")
#简洁二分支，注意他返回的是表达式
guess=eval(input())
print("猜{}了".format("对" if guess==99 else "错"))
#多分支 if : elif: else:
#保留字 and 与 or 或 not 非
#异常处理
'''
try:
  <语句1>
except<类型>:  类型可以不添加，添加之后表示只有这种类型异常出现才会执行语句2
  <语句2>  执行语句1出现异常，则执行语句2，不出现异常，执行1后跳过语句2'''
try:
    num=eval(input("请输入一个整数"))
    print(num**2)
except:
    print("输入不是整数")
