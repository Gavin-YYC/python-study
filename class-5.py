# coding=utf-8
class Test( object ):
    def __init__( self ):
        self.a = 1
    def __eq__( self, other ):
        if self.a == other.a:
            return True
        else:
            return False

t1 = Test()
t2 = Test()

print t1 == t2
# 输出结果：True
