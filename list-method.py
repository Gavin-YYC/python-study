# coding=utf-8

# 定义序列
names = [
    'Peter',
    'Gavin',
    'Yang Youcun',
    'Peter',
    'Shuai',
    'Huimin'
]

# 方法
print names
# 追加元素 append
print '追加元素"--""：' + `names.append('--')`

# 统计次数 count
print "统计Peter次数：" + names.count('Peter')

# 拓展数组 extend
print '追加"[1,2,3]"：' + names.extend([1,2,3])

# 元素索引 index
print '获得Yang Youcun在数组的索引位置：' + names.index('Yang Youcun')

# 插入方法 insert
print 







