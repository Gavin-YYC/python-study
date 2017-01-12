# Python 字符串

知识点梳理

![QQ20170112-164333@2x](http://7mj4a6.com1.z0.glb.clouddn.com/2017-01-12-QQ20170112-164333@2x.png)

## 一、基础操作

### 1、长度

```python
str = 'My name is Gavin'
len(str)
# 16
```
### 2、索引

```python
str = 'My name is Gavin'
str[12]
# 'a'
```

### 3、成员资格

```python
str = 'My name is Gavin'
'is' in str
# True
```

### 4、乘法

```python
str = 'hello'
str * 5
# 'hellohellohellohellohello'
```

### 5、分片

```python
str = 'My name is Gavin'
str[11:16]
# 'Gavin'
```

> 注意，分片是`[m, n)`的区间形式。

上述也可采用更优雅的形式：

```python
str = 'My name is Gavin'
str [11:20]
# 'Gavin'
```

也可以使用负数：

```python
str = 'My name is Gavin'
str[11:-4]
# 'G'
```

> 如果开始位置或结束位置为空，则将空值作为边界

```python
str = 'My name is Gavin'
str[:3]
# 'My '

str[-5:]
# 'Gavin'

# 也可以全部空，表示复制一遍
str[:]
# 'My name is Gavin'
```

#### 步长

表示每隔几个元素，普通步长默认为1。

```python
str = 'My name is Gavin'
str[::2]
# 'M aei ai'
```

## 二、处理方法：

### 1、find()

返回子串所在位置的最左端的索引。没有找到指定的字符串时，返回`-1`。

```python
longWorld = 'Hello, my name is Gavin'
longWorld.find('my')
# 7

longWorld.find.find('morning')
# -1
```

也可指定查找范围，可以给find添加第二或第三个参数：

```python
# 从第10个字符开始查找
longWorld = 'Hello, my name is Gavin, my job is xxx'
longWorld.find('my', 10);
# 25
```

### 2、split()

将字符串按指定分隔符分割成序列，没有分隔符时，默认是空格为分隔符。

```python
str = '1+2+3+4'
str.split('+')
# ['1', '2', '3', '4']
```

### 3.join()

将序列元素以指定字符串连接形成新的字符串，join是split的逆方法。

```python
arr = ['1', '2', '3', '4']
sep = '+'
sep.join( arr )
# '1+2+3+4'
```
> 注意：序列中的每一项必须是字符串。

### 4、strip()

去除字符串两侧空格（不包括中间空格）。

```python
str = ' my name is Gavin '
str.strip();
# 'my name is Gavin'
```

strip()也可以去除指定字符：

```python
str = '*** my name is *** Gavin ***'
str.strip('***')
# ' my name is *** Gavin '
```

上面中，去掉了前后的`***`，但是空格与中间的`***`依然保留。

python也提供了去除左边或者右边指定字符的方法：

* `rstrip()` 去除右边指定字符串
* `lstrip()` 去除左边指定字符串

### 5、lower()

将字符串全部转成小写。

```python
str = 'My name is Gavin'
str.lower()
# 'my name is gavin'
```

还有一些相似方法：

* `upper()` 全部字符转成大写字母

* `title()` 字符串转成标题（所有字母首字母大写）

```python
# 所有单词首字母大写
str = 'My name is Gavin'
str.title()
# 'My Name Is Gavin'
```
	
* `capitalize()` 将字符串第一个字母大写

```python
# 只有字符串第一个字母大写
str = 'My name is Gavin'
str.capitalize()
# 'My name is gavin'
```

### 6、replace()

替换字符串中的字符，返回被替换后的字符。

```python
str = 'My name is Tom'
str.replace('Tom', 'Gavin')
# 'My name is Gavin'
```

replace()方法除了两个必须参数外，还有一个参数：max，最多替换多少次：

```python
str = 'aaaaa'
str.replace('a', 'b', 2)
# 'bbaaa'
```

其他相似方法：

* `translate()` 根据table表转换字符

```python
from string import maketrans
old = 'aeiou'
new = '12345'
str = 'My name is Gavin'
table = maketrans(old, new)
str.translate( table )
# 'My n1m2 3s G1v3n'
```

translate()还有第二个参数，表示删除的字符。

### 7、format()

字符串格式化。提供字符串与占位符的映射关系。

```python
str = 'My name is {name}, My job is {job}'
str.format(name='Gavin', job='engineer')
# 'My name is Gavin, My job is engineer'
```

上面是通过关键字来对应映射关系，此外还可以通过位置进行映射。

```python
str = 'My name is {0}, My job is {1}'
str.format('Gavin', 'engineer')
# 'My name is Gavin, My job is engineer'
```

此外，还可以通过对象属性、队列下表进行映射。

```python
# 通过对象属性
class Person:
	def __init__( self ):
		self.name = 'Gavin'
		self.job = 'engineer'
	def __str__( self ):
		str = 'My name is {self.name}, My job is {self.job}'
		return str.format( self=self )


# 通过下标
ls = ['Gavin', 'engineer']
str = 'My name is {0[0]}, My job is {0[1]}'
str.format( ls )
# 'My name is Gavin, My job is engineer'
```

> 注意，这里的占位符通过`{}`来界定，这代替了之前版本的`%`。

## 三、验证方法

### 1、isdigit() -- 是否全部为数字组成

```python
'1234'.isdigit() # True
'12 34'.isdigit() # False，中间有空格
'dsqu212'.isdigit() # False，有其他字符
```

### 2、isalpha() -- 是否全部为字母

```python
'My name is Gavin'.isalpha() # False 有空格
'MynameisGavin'.isalpha() # True
'12d__d'.isalpha() # False 有其他字符
```

### 3、isalnum() -- 是否为字母或数字

```python
'123abd'.isalnum() # True
```

### 3、islower()、isupper() -- 是否全部为小/大写

### 4、istitle() -- 是否为title形式

### 5、isspace() -- 是否都是空白字符

```python
' '.isspace() # True
'\n\t\r '.isspace() # True
```

## 四、其他

### 1、输出长字符串

```python
print '''My name is Gavin,
my job is engineer.
This is a very long string.
It continues here.
still here.
over
'''
# My name is Gavin,
# my job is engineer.
# This is a very long string.
# It continues here.
# still here.
# over
```

### 2、转义

```python
print 'My name is \n Gavin'
# My name is
#  Gavin
```
使用`\`进行转义。

## 3、原始字符串

有些情况下，字符串中有转义字符，但又不想转义，可以使用原始字符串。

```python
# 没使用原始字符串
print 'C:\\window'
# 'C:\window'

# 使用原始字符串
print r'C:\\window'
# 'C:\\window'
```

获取原始字符串，只需添加`r`前缀即可。

## 4、Unicode字符串

python中的普通字符串在内部是以8位ASCII码形式存储的。Unicode为16位Unicode字符串。

在python3中，所有字符串都是unicode字符串。






