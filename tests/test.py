class MyNumber:
    def __init__(self, value):
        self.value = value

    # 定义加法魔术方法
    def __add__(self, other):
        return MyNumber(self.value + other.value*10)

    def __str__(self):
        return str(str(self.value)+"xxxx")



num1 = MyNumber(5)
num2 = MyNumber(3)
result = num1 + num2
print(result)  # 输出: 8
