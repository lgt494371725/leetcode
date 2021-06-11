user_data={'123':'aaa'}

def new_user():
    while True:
        name =input('请输入用户名：')
        if name in user_data:
            print('该用户名已经被使用')
        else:
            break
    passwd=input('请输入密码：')
    user_data[name]=passwd
    print("注册成功！")
def old_user():
    while True:
        name = input("请输入用户名：")
        if name not in user_data:
            print("您输入的用户名不存在！")
        else:
            break
    passwd=input("请输入密码：")
    if passwd==user_data[name]:
        print("登录成功！")
    else:
        print("密码错误")

def showmenu():
    prompt='''
|--- 新建用户：N/n ---|
|--- 登录账号：E/e ---|
|--- 退出程序：Q/q ---|
|--- 请输入指令代码：'''
    while True:
        while True:
            choice=input(prompt)
            if choice not in 'NnEeQq':
                print('输入的指令有误，请重新输入：')
            else:
                break
        if choice=='q'or choice=='Q':
            break
        if choice=='n'or choice=='N':
            new_user()
        if choice=='e'or choice=='E':
            old_user()
showmenu()









                
