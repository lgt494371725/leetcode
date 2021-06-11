
import time as t

class Mytimer:
    def __add__(self,other):
        prompt='总共运行了'
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt+=str(result[index])+self.unit[index]
        return prompt
    def __init__(self):
        self.unit=['年','月','天','小时','分钟','秒']
        self.prompt='未开始计时'
    #防止未计时前调用而出错
    def __str__(self):
        return self.prompt
    __repr__=__str__
    #这样就可以省去再次定义一个函数
    def start(self):
        self.begin=t.localtime()
        self.prompt="请先调用stop停止计时！"
        #注意localime返回的是一个时间元组
        print("计时开始！")
    def stop(self):
        if not self.begin:
            print("请先开始计时！")
        else:
            self.end=t.localtime()
            self._calc()
            print("计时结束！")
    def _calc(self):
        self.lasted=[]
        self.prompt='总共运行了'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
            #只加入非零的单位
                self.prompt+=str(self.lasted[index])+self.unit[index]
        #为下一轮计时进行初始化
        self.begin=0
        self.end=0 
#计时器2，利用内置函数准确计算
'''
import time as t

class MyTimer:
    def __init__(self):
        self.prompt = "未开始计时！"
        self.lasted = 0.0
        self.begin = 0
        self.end = 0
        self.default_timer = t.perf_counter
    
    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = "总共运行了 %0.2f 秒" % result
        return prompt
    
    # 开始计时
    def start(self):
        self.begin = self.default_timer()
        self.prompt = "提示：请先调用 stop() 停止计时！"
        print("计时开始...")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用 start() 进行计时！")
        else:
            self.end = self.default_timer()
            self._calc()
            print("计时结束！")

    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = self.end - self.begin
        self.prompt = "总共运行了 %0.2f 秒" % self.lasted
        
        # 为下一轮计时初始化变量
        self.begin = 0
        self.end = 0

    # 设置计时器(time.perf_counter() 或 time.process_time())
    def set_timer(self, timer):
        if timer == 'process_time':
            self.default_timer = t.process_time
        elif timer == 'perf_counter':
            self.default_timer = t.perf_counter
        else:
            print("输入无效，请输入 perf_counter 或 process_time")

'''
