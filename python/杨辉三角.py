def generate(numRows):
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret
num=eval(input("输入数字"))
list1=generate(num)
for i in list1:
    print(str(i).center(30))
#ljust,center,rjust,
