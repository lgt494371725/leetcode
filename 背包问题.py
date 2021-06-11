tr=[None,{'w':2,'v':3},{'w':3,'v':4},{'w':4,'v':8},{'w':5,'v':8},{'w':9,'v':10}]
#tr是列表类型，该顺序即代表第i个货物
max_w=20
#背包最大承重
#初始化二维表格m[(i,w)],注意是字典类型！
#表示前i个货物，最大重量w的组合中，所得到的最大价值
m={(i,w):0 for i in range(len(tr))
           for w in range(max_w+1)}
for i in range(1,len(tr)):#考虑第i件
    for w in range(1,max_w+1):#当前重量
        if tr[i]['w']>w:#背包装不下，tr[i]代表其中一个元素即字典，然后通过['w']访问字典，返回重量
            m[(i,w)]=m[(i-1,w)]
        else:
            m[(i,w)]=max(m[(i-1,w)],m[(i-1,w-tr[i]['w'])]+tr[i]['v'])

print(m[(len(tr)-1,max_w)])
