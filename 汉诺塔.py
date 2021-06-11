def hanoi(n,x,y,z):
    if n==1:
        print("{}-->{}".format(x,z))
    else:
        hanoi(n-1,x,z,y)
        print("{}-->{}".format(x,z))
        hanoi(n-1,y,x,z)

hanoi(3,'X','Y','Z')
