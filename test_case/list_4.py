# coding=utf-8

# 检查用户名和密码
database = [
    ['albert', '1234'],
    ['dilbert', '1232'],
    ['smith', '4322'],
    ['jones', '3241']
]

username = raw_input("User name: ")
pin = raw_input('Pin code: ')

if [username, pin] in database: print "Accrss granted"
