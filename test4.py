# coding=utf-8
allItems = [
    'pepperoni',
    'sausage',
    'cheese',
    'peppers'
]

item = raw_input('请输入您喜欢的配料：')

if item in allItems:
    print [ item  ]
else:
    print 'sorry'
