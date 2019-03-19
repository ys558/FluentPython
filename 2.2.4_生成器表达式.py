symbols = '☚☟♫☯☳'

# 2.5 生成器表达式tuple,array
tuple = tuple(ord(symbol) for symbol in symbols)
print(tuple)
# (9754, 9759, 9835, 9775, 9779)
import array
array = array.array('I', (ord(symbol) for symbol in symbols))
print(array)
# array('I', [9754, 9759, 9835, 9775, 9779])

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s, %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
# black, S
# black, M
# black, L
# white, S
# white, M
# white, L
