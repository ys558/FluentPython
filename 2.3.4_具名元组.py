# 2-9 定义和使用具名元组
from collections import namedtuple

# 1. 基础：
City = namedtuple('City', 'name country population coordinates')
# 把'name country population coordinates'里各个值依次赋值，
# 所以City里的字段必须一一对应，否则报错
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo)
## City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))

# 2. 取值，取键：
# 除了像字典的的键值对一样用.取值之外，还能用下标[x]取值
print(tokyo.coordinates)
## (35.689722, 139.691667)
# print(tokyo[2])
## 36.933
# 键名用._fields取，他是一个包含这个类所有字段名称的元组
print(City._fields)
## ('name', 'country', 'population', 'coordinates')

# 3. 几个具名元组的方法：
# 具名元组细化嵌套：
LatLong = namedtuple('LatLong', 'lat long')
NewYork_data = ('NewYork', 'US', 20.104, LatLong(19.433333, -74.020386))
# _make方法和City(*NewYork_data)作用一样，通过接收一个可迭代对象生成一个新的实例
NewYork = City._make(NewYork_data)
# ._asdict()生成一个OrderedDict：
# print(NewYork._asdict())
# OrderedDict([('name', 'NewYork'), ('country', 'US'), ('population', 20.104), ('coordinates', LatLong(lat=19.433333, long=-74.020386))])

# .items()可直接遍历每个元素，将其变成可循环的字典：
for key, value in NewYork._asdict().items():
    print(key + ':', value)
