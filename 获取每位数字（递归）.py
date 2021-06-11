term=[]
def getdigit(number):
        if number:
            term.insert(0,number%10)
            getdigit(number//10)
getdigit(12345)
print(term)
    
