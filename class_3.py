# coding=utf-8

class Student( object ):
    def __init__( self, name = '', school = '', grade = '' ):
        if not name:
            name = raw_input('输入学生姓名：')
        if not school:
            school = raw_input('输入该学生学校：')
        if not grade:
            grade = self.get_grade()

        self.name = name
        self.school = school
        self.grade = grade

    def get_grade( self ):
        while True:
            grade = raw_input('请输入学生成绩：')
            if grade.lower() not in ['k', '1', '2', '3', '4', '5']:
                print '{}无效'.format( grade )
            else:
                return grade

    def print_student( self ):
        print 'Name: {}'.format( self.name )
        print 'School: {}'.format( self.school )
        print 'Grade: {}'.format( self.grade )

def print_roster( students ):
    print '学生列表：'
    for student in students:
        print "*" * 15
        student.print_student()

def main():
    student1 = Student( name="a", school='s1', grade='3' )
    student2 = Student( name="b", school='s2', grade='k'  )
    student3 = Student( name="c", school='s3', grade='2'  )
    students = [ student1, student2, student3 ]
    print_roster( students )

if __name__ == '__main__':
    main()
