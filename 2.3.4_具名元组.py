from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo)
## City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
# print(tokyo[2])
## 36.933
# print(tokyo.coordinates)
## (35.689722, 139.691667)

# print(City._fields)
# # _fields属性是一个包含这个类所有字段名称的元组
## ('name', 'country', 'population', 'coordinates')

LatLong = namedtuple('LatLong', 'lat long')
NewYork_data = ('NewYork', 'US', 20.104, LatLong(19.433333, -74.020386))
# _make方法和City(*NewYork_data)作用一样，通过接收一个可迭代对象生成一个新的实例
NewYork = City._make(NewYork_data)
print(NewYork._asdict())

for key, value in NewYork._asdict().items():
    print(key + ':', value)
