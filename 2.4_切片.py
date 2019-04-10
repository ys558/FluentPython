# 基础：
# [开始:结束:间隔的步长]
# 3个值均可为负数，含“开始”的数字，不含“结束”的数字，即含前不含后

l = [10,20,30,40,50,60]
# 利用 [:x]和[x:]把数组变成两段：含冒号前面数字不含后
# print(l[:2])
# [10, 20]
# print(l[2:])
# [30, 40, 50, 60]

s = 'bicycle'
# print(s[::3])
# bye
# [::-1]可实现直接翻转整个：
# print(s[::-1])
# elcycib
# print(s[::-2])
# eccb

# slice(a,b,c)方法, a,b,c对应start,end,step
invoice = """
1909 Pimoroni PiBrella             $17.50   3   $52.50
1601 PiTFT Mini Kit 320x240        $34.95   1   $34.95
1489 6mm Tacticle Switch x20       $4.95    2   $4.95
"""
sku = slice(0,4)
description = slice(4, 34)
unit_price = slice(34, 43)
quantity = slice(43, 46)
total = slice(46, 52)
line_items = invoice.split('\n')
for item in line_items:
    print(item[unit_price], item[description])
#  $17.50    Pimoroni PiBrella
#  $34.95    PiTFT Mini Kit 320×240
#  $4.95     6mm Tacticle Switch ×20

# 2.4.3 多维切片，numpy库

# 2.4.4 切片赋值
l = list(range(10))
# print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5]=[20,30,100,200]
# 意思是把2到5拿掉(不含5)，替换成20,30,100,200
# print(l)
# [0, 1, 20, 30, 100, 200, 5, 6, 7, 8, 9]
del l[5:7]
# print(l)
# [0, 1, 20, 30, 100, 6, 7, 8, 9]

# 玩玩嵌套列表：
board = [['_']*3 for i in range(3)]
# print(board)
# [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 'x'
# print(board)
# [['_', '_', '_'], ['_', '_', 'x'], ['_', '_', '_']]

# 关于列表嵌套的乘法：
weird_board = [['_']*3]*3
print(weird_board)
# [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
weird_board[1][2] = '0'
# *的方法对于列表的引用是指向同一对象：输出如下：所以列表的*方法慎用
print(weird_board)
# ['_', '_', '0'], ['_', '_', '0'], ['_', '_', '0']]
