#dayup down
dayup=pow(1.001,365)
daydown=pow(0.999,365)
print("向上：{:.2f},向下{:.2f}".format(dayup,daydown))
#dayup down factor
dayfactor=0.005
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365)
print("向上：{:.2f},向下{:.2f}".format(dayup,daydown))

#dayup down Q3
dayup=1.0
dayfactor=0.01
for i in range(365):    
    if i%7 in [6,0]:
        dayup=dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print("工作日的力量:{:.2f}".format(dayup))

#dayupdown Q4,利用函数
def dayUP(df):
    dayup=1
    for i in range(365):    
        if i%7 in [6,0]:
            dayup=dayup*(1-df)
        else:
            dayup=dayup*(1+df)
    return dayup
dayfactor=0.01
while dayUP(dayfactor)<37.78:
    dayfactor+=0.001
print("工作努力参数：{:.3f}".format(dayfactor))

