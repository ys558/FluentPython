# 2.3.2 元组拆包
lax_coordinates = (33.9425, -118.408056)
latitude, longtitude = lax_coordinates
# print(latitude)
# print(longtitude)
# 33.9425
# -118.408056

# print(divmod(20,8))
# divmod求商和余数，这里表示是2余4
# (2, 4)

# 上面的divmod可以改写为元组拆包：
t = (20, 8)
quotient, remainder = divmod(*t)
# print(remainder)
# # 4

# os.path.split()模块中，解析路径，可以生成（path, last_part）的元组
import os
_, filename = os.path.split('/home/aaa/.ssh/idrsa.pub')
# print(_,filename)
# # /home/aaa/.ssh idrsa.pub

# *接收剩余的元素
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
