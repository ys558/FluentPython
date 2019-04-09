# 2.3.2 元组拆包
lax_coordinates = (33.9425, -118.408056)
# 平衡赋值，实现拆包：
latitude, longtitude = lax_coordinates
print(latitude)
# 33.9425
print(longtitude)
# -118.408056

print(divmod(20,8))
# divmod求商和余数，这里表示是2余4
# (2, 4)
# 上面的divmod可以改写为元组拆包：
t = (20, 8)
# 平衡赋值实现拆包：
quotient, remainder = divmod(*t)
print(remainder)
# 4
print(quotient)
# 2

# 具体应用场景：
# os.path.split()模块中，解析路径，可以生成（path, last_part）的元组
import os
_, filename = os.path.split('/home/aaa/.ssh/idrsa.pub')
# print(_, filename)
# # /home/aaa/.ssh idrsa.pub

# 用*接收剩余的元素, 以下是ipython的输出结果：
# # ipython交互模式下运行:
# In [16]: a, b, *rest = range(5)
# In [17]: a, b, rest
# Out[17]: (0, 1, [2, 3, 4])

# In [14]: a, *body, c, d = range(5)
# In [15]: a, body, c, d
# Out[15]: (0, [1, 2], 3, 4)

# In [18]: *head, b, c, d = range(5)
# In [19]: head, b, c, d
# Out[19]: ([0, 1], 2, 3, 4)

# 2.3.3 嵌套元组拆包：
metro_area = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Mexico City', 'MX', 20.142, (19.43333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
]
# 直接用(latitude, longtitude)和第四个元素对应
for name, cc, pop, (latitude, longtitude) in metro_area:
    # 打印时取需要的字段即可：
    print(name, latitude, longtitude)

# Tokyo 35.689722 139.691667
# Mexico City 19.43333 -99.133333
# New York-Newark 40.808611 -74.020386
