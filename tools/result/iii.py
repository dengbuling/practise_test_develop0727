# 相对路径
from yyy import x1

# 将函数x1和参数(4,4)扔到broker中
result = x1.delay(4,4)
print(result.id)