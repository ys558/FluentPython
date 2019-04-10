# +=的背后方法是__iadd__，就地加法，
# 对于可变序列，这种方法不会开辟一块新的内存，如果一个类没有__iadd__，
# python会退一步调用__add__
# 例如：a+=b就是调用了__iadd__方法,a=a+b就调用了__add__方法
# 当然，*=，-=，/=也是一样的道理
# 下面是例子:

# 可以看到两个内存地址是一样的
l = [1,2,3]
print(id(l))
# 30696008
l *= 2
print(id(l))
# 30696008

# 当然，对于不可变序列的元组，
# 内存地址还是会改变：证明元组没有__iadd__方法，只有__add__方法
t = (1,2)
print(id(t))
# 7484040
t *= 2
print(id(t))
# 7117544

# 谜题：不可变序列套着可变序列下的就地加法
# 以下必须在交互模式：
# In [10]: t = (1,2,[30,40])

# In [11]: t[2] += [50, 60]
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-11-d877fb0e9d36> in <module>
# ----> 1 t[2] += [50, 60]

# TypeError: 'tuple' object does not support item assignment

# In [12]: t
# Out[12]: (1, 2, [30, 40, 50, 60])
# 这里的t虽然抛出异常，但依旧被改动
# 这里虽然可以改成t[2].extend([50,60])，
# 但为了说明问题，用代码分析模块dis以下例子：

import dis
print(dis.dis('s[a] += b'))
#   1           0 LOAD_NAME                0 (s)
#               2 LOAD_NAME                1 (a)
#               4 DUP_TOP_TWO
#               6 BINARY_SUBSCR
#               8 LOAD_NAME                2 (b)
#              10 INPLACE_ADD
#              12 ROT_THREE
#              14 STORE_SUBSCR
#              16 LOAD_CONST               0 (None)
#              18 RETURN_VALUE
# None
# 到14 STORE_SUBSCR时，因为s是不可变元组，所以返回None

# 2.7 列表的就地排序sorted, list.sort
fruits = ['grape', 'apple', 'banana','orange']
print(sorted(fruits, key=len, reverse=True))
# ['banana', 'orange', 'grape', 'apple']
print(fruits)
# ['grape', 'apple', 'banana', 'orange']
# fruits没变，证明改方法是就地排序
