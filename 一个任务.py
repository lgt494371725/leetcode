def save_file(boy,girl,count):
        file_name_boy='boy'+str(count)+'.txt'#每个文件的名字
        file_name_girl='girl'+str(count)+'txt'
        boy_file=open(file_name_boy.'w')
        girl_file=open(file_name_girl.'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)
        boy_file.close()
        girl_file.close()
f=open('record.txt')
#不写明地址则表明两份文件在同一目录下
boy=[]
girl=[]
count=1

for each_line in f:
    if each_line[:6]!='======':#判断前6个是不是等号即可
        term=each_line.split(':',1)#根据冒号分成2个子字符串并以列表形式返回
        if term[0]=='小甲鱼':
            boy.append(term[1])
        if term[0]=='小客服':
            girl.append([term[1])
    else:
        save_file(boy,girl,count)
        #重置并计数
        boy=[]
        girl=[]
        count+=1

save_file(boy,girl,count)
f.close()
