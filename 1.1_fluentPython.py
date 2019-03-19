import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    # 重写__len__ 定义这个类的长度：
    def __len__(self):
        return len(self._cards)

    # 重写__getitem__
    def __getitem__(self, position):
        return self._cards[position]



beer_card = Card('4', 'spades')
print(beer_card)
## Card(rank='4', suit='spades')

deck = FrenchDeck()
# 拿这叠纸牌里倒数第二张，列表表达式生成的纸牌已经放在内存里按顺序放好了
print(deck[-2])
## Card(rank='K', suit='hearts')

from random import choice
print(choice(deck))
# # 每次执行显示都不一样：
# # Card(rank='6', suit='diamonds')

# 切片：
# 最后3张
print(deck[:3])
# # [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
# 第12张开始：拿1张（默认1，可以不写）：隔13张
print(deck[12::13])
# # [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

# 反向迭代
# for card in reversed(deck):
#     print(card)

#   布尔判断：
print(Card('I', 'spades') in deck)
# # False

# 定义花色权重，把纸牌除了数字之外，加上花色重排大小
suit_values = dict(spades=3, hearts=2, diamonds=0, clubs=1)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
    
for card in sorted(deck, key = spades_high):
    print(card)

# Card(rank='2', suit='diamonds')
# Card(rank='2', suit='clubs')
# Card(rank='2', suit='hearts')
# Card(rank='2', suit='spades')
# Card(rank='3', suit='diamonds')
# Card(rank='3', suit='clubs')
# Card(rank='3', suit='hearts')
# Card(rank='3', suit='spades')
# Card(rank='4', suit='diamonds')
# Card(rank='4', suit='clubs')
# Card(rank='4', suit='hearts')
# Card(rank='4', suit='spades')
# Card(rank='5', suit='diamonds')
# Card(rank='5', suit='clubs')
# Card(rank='5', suit='hearts')
# Card(rank='5', suit='spades')
# Card(rank='6', suit='diamonds')
# Card(rank='6', suit='clubs')
# Card(rank='6', suit='hearts')
# Card(rank='6', suit='spades')
# Card(rank='7', suit='diamonds')
# Card(rank='7', suit='clubs')
# Card(rank='7', suit='hearts')
# Card(rank='7', suit='spades')
# Card(rank='8', suit='diamonds')
# Card(rank='8', suit='clubs')
# Card(rank='8', suit='hearts')
# Card(rank='8', suit='spades')
# Card(rank='9', suit='diamonds')
# Card(rank='9', suit='clubs')
# Card(rank='9', suit='hearts')
# Card(rank='9', suit='spades')
# Card(rank='10', suit='diamonds')
# Card(rank='10', suit='clubs')
# Card(rank='10', suit='hearts')
# Card(rank='10', suit='spades')
# Card(rank='J', suit='diamonds')
# Card(rank='J', suit='clubs')
# Card(rank='J', suit='hearts')
# Card(rank='J', suit='spades')
# Card(rank='Q', suit='diamonds')
# Card(rank='Q', suit='clubs')
# Card(rank='Q', suit='hearts')
# Card(rank='Q', suit='spades')
# Card(rank='K', suit='diamonds')
# Card(rank='K', suit='clubs')
# Card(rank='K', suit='hearts')
# Card(rank='K', suit='spades')
# Card(rank='A', suit='diamonds')
# Card(rank='A', suit='clubs')
# Card(rank='A', suit='hearts')
# Card(rank='A', suit='spades')
