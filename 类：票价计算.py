class Ticket():
    def __init__(self,weekend=False,child=False):
        self.base=100
        if weekend:
            self.factor1=1.2
        else:
            self.factor1=1
        if child:
            self.factor2=0.5
        else:
            self.factor2=1
    def calprice(self):
        return self.base*self.factor1*self.factor2

adult=Ticket()
child=Ticket(child=True)
print("2个成人+1个小孩的平日票价为：{}".format(2*adult.calprice()+child.calprice()))
