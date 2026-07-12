# collections - Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

# 1. Counter
string = "aaaaabbbbbccc"

my_counter = Counter(string)

# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())

# # most_common()
# print(my_counter.most_common(2))

# # elements()
# print(list(my_counter.elements()))

# for ch in my_counter.elements():
#     print(ch)

# 2. namedtuple - replacement for simple class -- very easy to use and declare

# from collections import namedtuple

# Point = namedtuple('Point', 'x,y')

# pt = Point(4,5)

# print(pt, type(pt))
# print(pt.x, pt.y)

# 3. OrderDict

# from collections import OrderedDict

# myOrderedDict =  OrderedDict()
# myOrderedDict['b'] = 1
# myOrderedDict['a'] = 2
# myOrderedDict['c'] = 3
# myOrderedDict['e'] = 4
# myOrderedDict['d'] = 5

# print(myOrderedDict)

# 4. defaultdict

# from collections import defaultdict

# d = defaultdict(float)

# d['a'] = 1
# d['b'] = 2

# print(d)
# print(d['a'], d['b'])
# print(d['c'])

# 5. deque() --> Double Ended Queue

from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)

d.pop()
d.popleft()

d.extend([4, 5, 6])
d.extendleft([7, 8, 9])

d.rotate(1)
d.rotate(-1)

print(d)
