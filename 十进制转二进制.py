
temp=[]
def binary(decimal):
    result=''
    while decimal:
        a=decimal%2
        decimal//=2
        temp.append(a)
    while temp:
        result+=str(temp.pop())
    return result
print(binary(10))
