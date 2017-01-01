# coding=utf-8

# 创建基类
class School( object ):
    name = ''
    address = ''
    def print_school( self ):
        print self.name
        print self.address

# 实例化对象
school1 = School()
school2 = School()

# 现在学校还是空的，修改一下，给它们名称与地址
school1.name = '北京大学'
school1.address = '不知道'
school2.name = '清华大学'
school2.address = '依然不知道'

# 最后，输出学校信息
school1.print_school()
school2.print_school()

# 输出信息
# 北京大学
# 不知道
# 清华大学
# 依然不知道
