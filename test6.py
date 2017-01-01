# coding=utf-8

nameList = ['a', 'b', 'c', 'd']

def name_in_class( name ):
    return name in nameList

def main():

    print 'Welcome to the student checker!'

    while True:
        name = raw_input("Please give me the name of a student (enter 'q' to quit): [student1]")

        if name == 'q':
            print 'Goodbye!'
            break

        if name_in_class( name ):
            print 'Yes, that student is enrolled in the class!'
        else:
            print 'No, that student is not in the class!'

     

if __name__ == '__main__':
    main()
