# coding=utf-8

def save_student( nameList, uid, name, grade ):
    nameList[uid] = {
        "name": name,
        "grade": grade
    } 

def print_student(nameList):
    print "student" + '    ' + 'Grade'
    for item in nameList:
        print nameList[ item ]['name'] + '   ' + nameList[ item  ]['grade']

def main():
    uid = 0
    nameList = {}
    while True:
        name = raw_input("Please give me the name of the student (q to quit): ")

        if name == 'q':
           break

        grade = raw_input("Please give me their grade: ")

        save_student( nameList, uid, name, grade )
        uid = uid + 1


    print_student(nameList)
    

if __name__ == '__main__':
    main()
