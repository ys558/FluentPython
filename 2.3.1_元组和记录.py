# 坐标：
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
travaler_ids = [('USA', '31195855'),
                ('BRA', 'CE342567'),
                ('ESP', 'XDA205856')]

for passport in sorted(travaler_ids):
    print('%s/%s'%passport)
# BRA/CE342567
# ESP/XDA205856
# USA/31195855

for country, _ in travaler_ids:
    print(country)
# USA
# BRA
# ESP
