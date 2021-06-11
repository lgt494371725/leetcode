def anagramsolution1(s1,s2):
    alist=list(s2)
    #将字符串列表化
    pos1=0
    stillOK=True
    while pos1<len(s1) and stillOK:
        #循环s1每个字符
        pos2=0
        found=False
        while pos2<len(alist) and not found:
            if s1[pos1]==alist[pos2]:
                found=True
        #在s2中逐个对比
            else:
                pos2=pos2+1
        if found:
            alist[pos2]=None
        else:
            stillOK=False
            #未找到
        pos1=pos1+1
        
    return stillOK
def anagramsolution2(s1,s2):
    alist1=list(s1)
    alist2=list(s2)
    alist1.sort()
    alist2.sort()
    pos=0
    matches=True
    while pos<len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos+=1
        else:
            matches=False
    return matches

def amagramsolution3(s1,s2):
    c1=[0]*26
    c2=[0]*26
    for i in range(len(s1)):
        pos=ord(s1[i])-ord('a')
        #通过CODE相减把字母保存到列表对应的0—25
        c1[pos]=c1[pos]+1
    for i in range(len(s2)):
        pos=ord(s2[i])-ord('a')
        c2[pos]+=1
    #ord能够将字母转化成对应的UNICODE码
    j=0
    stillOK=True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j+=1
        else:
            stillOK=False
    return stillOK
print(anagramsolution2('python','typhon'))



































    
