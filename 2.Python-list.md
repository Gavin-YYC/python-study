# Python 列表

知识点梳理

![屏幕快照-2017-01-12-16.51.32](http://7mj4a6.com1.z0.glb.clouddn.com/2017-01-12-屏幕快照-2017-01-12-16.51.32.png)


数据结构是按照一定的方式组织在一起的数据元素的集合。这些数据元素可以是数字或者字符串，甚至可以是其他数据结构，在Python中，最基本的额数据结构是序列。

Python共有6种内建序列，最常用的是列表有元组，其他还有字符串、Unicode字符串、buffer对象和xrange对象。

序列和元组的主要区别是，序列可以修改，元组不可修改。

## 列表

如下列表，表示个人信息，第一项是username，第二项是job。

	user = ['Gavin', 'engineer']

也可以构建用户数据库：

	database = [['Gavin', 'engineer'], ['john', 'artist']]

## 列表通用操作

因为字符串也是一个序列，对字符串序列的操作在列表上同样适用，是通用操作方法。

### 1、索引

```python
user = ['Gavin', 'engineer']
user[0]
# 'Gavin'
user[1]
# 'engineer'
```

第一项索引为0，最后一项索引为-1。

```python
user = ['Gavin', 'engineer']
user[1] == user[-1]
# True
```

### 2、分片

索引用来访问单个元素，分片用来访问一段范围的元素。

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbers[3:5]
# [4, 5]
```

分片规则依然是`[m: n)`

现在，访问最后三项：

```python
# 显示访问
numbers[7: 10]
# 或者
numbers[-3:]
```

采用第二个参数为空的形式，表示到达最后一个元素

也可第一个参数为空，表示从第一个元素开始

```python
numbers[:3]
# [1, 2, 3]
```

那么，如果是全空，则表示从头到尾。

```python
numbers[:]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
```
#### 步长

分片操作还有第三个参数，表示步长，默认为1，表示按照这个步长遍历元素，也可显示设置。

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbers[1:5:2]
# [2, 4]
```

步长也可以是负数，表示从右向左提取元素。可以实现倒序输出

```python
# 下面的方式无法获取到范围
numbers[8:3]
# []

# 可以使用步长
numbers[8:3:-1]
# [9, 8, 7, 6, 5]
```

### 3、序列相加

只有同种类型的序列才可相加，不同种类型相加会出错。

```python
[1, 2, 3] + [4, 5, 6]
# [1, 2, 3, 4, 5, 6]
```

### 4、乘法

数字X乘以序列，序列重复X次

```python
numbers = [1, 2, 3]
3 * numbers
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

空序列：`[]`

初始化长度为10的序列：

```python
[None] * 10
```

### 5、成员资格

元素是否在序列中，同样使用`in`操作符。

```python
user = ['Gavin', 'engineer']
'Gavin' in user
# True
```

同样可用于判断列表：

```python
user = ['Gavin', 'engineer']
database = [['Gavin', 'engineer'], ['John', 'artisr']]
user in database
# True
```

### 6、长度、最大/小值

内建函数：`len()`、`max()`、`min()`

```python
numbers = [1, 2, 3, 4, 5, 6, 7]

# 长度
len( numbers )
# 2

# 最大值
max( numbers )

# 最小值
min( numbers )
```

## 列表操作

列表不同是元组，列表是可变的，改变列表的长度或元素，需要一些操作方法（增删改查），这里进行列举：

### list()函数

将字符串转成列表。

```python
list('python')
# ['p', 'y', 't', 'h', 'o', 'n']
```

### 元素赋值

```python
ls = [1, 2, 3]
ls[2] = 4
ls
# [1, 2, 4]
```

### 删除元素

```python
ls = [1, 2, 3]
del ls[2]
ls
# [1, 2]
```

### 分片赋值

```python
ls = [1, 2, 3]
# 分片赋值可以增加元素，不删除元素
ls[1:1] = [2]
# [1, 2, 2, 3]

# 分片赋值可以增加元素，替换掉2
ls = [1, 2, 3]
ls[1:2] = [4, 5]
# [1, 4, 5, 3]

# 也可使用分片赋值删除元素
ls[1:2] = []
# [1, 5, 3]
```

### 列表方法

### 1、append()

在列表末尾追加元素。

```python
lst = [1, 2, 3]
lst.append(4)
lst
# [1, 2, 3, 4]
```

### 2、count()

统计列表中元素出现的次数

```python
lst = [1, 2, 3, 4, 4, 2, 2, 5]
lst.count(4)
# 2
```

### 3、extend()

向列表的末尾一次性追加多个值，用新列表扩充原列表。extend()只接收一个数组。

```python
lst = [1, 2, 3]
lst.extend([4, 5, 6])
lst
# [1, 2, 3, 4, 5, 6]
```

> 该操作和`列表相加`功能类似，但有区别，lst会拓展原数组，`+`会返回新数组。

```python
lst = [1, 2, 3]
lst + [4, 5, 6]
# [1, 2, 3, 4, 5, 6]
lst
# 原列表没有改变
# [1, 2, 3]

# extend改变原列表
lst.extend([4,5,6])
# lst
# [1, 2, 3, 4, 5, 6]
```

### 4、index()

返回某一元素第一次出现的索引。

```python
lst = [1, 2, 3, 2]
lst.index(2)
# 1
```

当元素不在列表中时，会出错，所以，一般获取某元素的索引，可以使用安全的验证方法：

> 此处和JavaScript不一样，在JavaScript中，index获取不到时，返回-1。

```python
if 5 in lst and lst.index(5):
	print lst.index(5)
```

### 5、insert()

将对象插入到列表中。

```python
numbers = [1, 2, 3]
numbers.insert(1, 'haha')
numbers
# [1, 'haha', 2, 3]
```

### 6、pop()

移除列表中的最后一个元素，并返回该元素的值。

```python
numbers = [1, 2, 3]
numbers.pop()
# 1 
```

也可删除指定位置的元素：

```python
# 删除index为2的元素
numbers = [1, 2, 3]
numbers.pop(1)
# 2
```

栈是常见的数据结构，特点是后进先出。下面通过列表方法模拟：

```python
numbers = [1, 2, 3]
numbers.append(4)
numbers.pop()
# [1, 2, 3]
```

队列：先进先出

```python
numbers = [1, 2, 3]
numbers.append(4)
numbers.pop(0)
# [2, 3, 4]
```

### 7、remove()

移除列表中的某个值，只移除匹配到的第一个

```python
numbers = [1, 2, 3, 2]
numbers.remove(2)
# [1, 3, 2]
```

> remove()和pop()类似，都是删除元素，但两者存在区别
> 1、pop()有返回值，remove()没有返回值
> 2、pop()根据index删除值，remove()通过值进行删除

### 8、reverse()

将列表元素倒置。

```python
numbers = [1, 2, 3]
numbers.reverse()
# [3, 2, 1]
```

### 9、sort()

对列表排序，会改变原列表，`并不返回值`

```python
numbers = [1, 3, 53, 2, 43, 23]
numbers.sort()
# [1, 2, 3, 23, 43, 53]
```

刚才说了，sort()不返回任何值，所以下列操作是错误的：

```python
ls = [1, 3, 2]
y = ls.sort()
print y
# None
```

实现上述方法的正确操作为：

```python
ls = [1, 3, 2]
y = ls[:]
y.sort()
print y
# [1, 2, 3]
```

#### 高级排序

sort()函数默认是升序排序，也可以自定义比较函数进行排序。

> Python提供了内建函数`cmp(x, y)`
> x > y 时，返回1
> x = y 时，返回0
> x < y 时，返回-1

```python
cmp(1, 2) # -1
cmp(1, 1) # 0
cmp(2, 1) # -1

# sort默认使用cmp进行排序
```

下面用自定义比较函数，进行降序输出：

```python
def compare( x, y ):
	if x > y:
		return -1
	elif x == y:
		return 0
	else:
		return 1

numbers = [1, 3, 2, 5, 4]
numbers.sort( compare )
# [5, 4, 3, 2, 1]
```

sort()函数还支持两个可选的`关键字参数`：`key`与`reverse`

* reverse 是否反向排序，True 或者 False

```python
numbers = [1, 3, 2, 5, 4]
numbers.sort(reverse=True)
# [5, 4, 3, 2, 1]
```

该参数的效果和上述自定义降序输出的效果相同。

* key 为每个元素创建一个键，然后所有元素按照键来排序

```python
# 按照长度进行排序
x = ['a', 'bbb', 'aa']
x.sort(key=len)
# ['a', 'aa', 'bbb']
```







