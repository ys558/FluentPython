symbols = '☚☟♫☯☳'

codes = []
for symbol in symbols: codes.append(ord(symbol))
print(codes)
# [9754, 9759, 9835, 9775, 9779]

# 直接用列表推导式的方法，读起来比上面的传统方法更容易读懂：
codes = [ord(symbol) for symbol in symbols]
print(codes)
# [9754, 9759, 9835, 9775, 9779]

# 列表推导式里也能加条件判断：
beyond_ascii = [ord(s) for s in symbols if ord(s) > 9775]
print(beyond_ascii)
# [9835, 9779]

# 使用map、filter函数
# map函数一一对应的生成：map(规则，要转换的对象)
beyond_ascii = list(filter(lambda c:c>9775, map(ord, symbols)))
print(beyond_ascii)
# [9835, 9779]
