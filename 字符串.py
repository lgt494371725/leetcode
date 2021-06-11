#字符串[M:N],M缺失表示到开头，N缺失表示到结尾
#字符串[M:N:K],根据步长K对字符串切片
print("0123456789"[:3])#012

print("0123456789"[1:8:2])#1357
print("0123456789"[::-1])#逆序表示字符串
#转义符\ 表达字符的本意。\n表示换行，\b表示回退 \r回车，光标回到本行首
print("这里有个双引号(\")")
'''字符串操作符
 x+y，连接两个字符串  n*x或者x*n,复制n次字符串x  x in s 判断x是不是s的字串，是则返回True'''

#获取星期
Weekstr="星期一星期二星期三星期四星期五星期六星期日"
Weekid=eval(input("请输入数字"))
pos=(Weekid-1)*3
print(Weekstr[pos:pos+3])
#获取星期，更简洁的写法
Weekstr="一二三四五六七"
weekid=eval(input("请输入数字:"))
pos=weekid-1
print("星期"+Weekstr[pos])

#len(x),返回字符串长度   str(x),将任意类型x转换为字符串类型，跟eval作用相反
#hex(x),oct(x).将整数x转换为十六进制或八进制字符串
#chr(u),u为unicode编码，返回其对应字符，ord(x),x为字符，返回其unicoude编码

#字符串处理方法
#str.lower() 或者str.upper()，切换大小写,如"AbCd".lower()结果为"abcd"
#str.split(sep),返回一个列表，由str根据sep被分割的部分组成，"A，B，C".split(",")结果为['A','B','C']
#str.count(sub)，返回字串sub在str中的出现次数。"an apple".count('a')结果为2
#str.replace(old,new)，将字符串中所有old替换成new并返回
#str.center(width,[fillchar]),字符串根据宽度width居中，fillchar在旁边。"python",centor(20,"=")结果为'========python======='
#str.strip(chars),除去字符。"= python=".strip(" =np")结果为“ytho”
#str.join(iter)   ",".join("12345")="1,2,3,4,5"
