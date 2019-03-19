from math import hypot

# 自定义向量类：
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)'%(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)

    def __pow__(self, index):
        return Vector(self.x**index, self.y**index)

    
v1 = Vector(2,4)
v2 = Vector(2,3)
print(v1+v2)
# Vector(4, 7)
print(abs(v1))
# 4.47213595499958
print(v2*3)
# Vector(6, 9)
print(v2**3)
# Vector(8, 27)
# # 1.2.2
# # 如果把 def __repr__(self):方法注销掉，控制台则输出表达式的内存地址
# # <__main__.Vector object at 0x00000000021E5A90>
# #　4.47213595499958
# # <__main__.Vector object at 0x00000000021E5A90>
# # <__main__.Vector object at 0x00000000021E5A90>
