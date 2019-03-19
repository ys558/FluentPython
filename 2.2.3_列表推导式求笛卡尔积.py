colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
# [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]

# 遍历出来：
for color in colors:
    for size in sizes:
        print((color, size))
# ('black', 'S')
# ('black', 'M')
# ('black', 'L')
# ('white', 'S')
# ('white', 'M')
# ('white', 'L')
