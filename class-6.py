# coding=utf-8

class InventoryItem( object ):
    def __init__( self, title = '', description = '', price = '' ):
        self.title = title
        self.description = description
        self.price = price

    # 打印时，打印标题
    def __str__( self ):
        return self.title

    # 对比时，比较书名
    def __eq__( self, other ):
        if self.title == other.title:
            return True
        else:
            return False

    # 改变标题
    def change_title( self, title ):
        if not title:
            title = raw_input('请输入标题：')
        self.title = title

    # 改变描述
    def change_description( self, description ):
        if not description:
            description = raw_input('请输入描述：')
        self.description = description


class Book( InventoryItem ):
    def __init__(self, title, description, price, author, format ):
        super(Book, self).__init__(title = title,
          description = description,
          price  = price)
        self.author = author
        self.format = format

    def __str__( self ):
        book_line = "{title} by {author}".format(
            title = self.title,
            author = self.author
        )
        return book_line

    def __eq__( self, other ):
        if self.title == other.title and self.author == other.author:
            return True
        else:
            return False

book1 = Book( title="a", description='d1', price='12', author='q', format='f')
book2 = Book( title="b", description='d2', price='24', author='23q', format='3f')


print book1
print book2
