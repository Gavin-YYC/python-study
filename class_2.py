# coding=utf-8

# 创建学生基类
class Student( object ):
    def __init__( self, name = '', age = 0 ):
        self.name = name
        self.age = age

student1 = Student( name = "Gavin", age = 26 )
student2 = Student( name = "YYC", age = 18)

print student1.name
print student1.age

print student2.name
print student2.age
