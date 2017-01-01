# coding=utf-8
inventory = [
    'butter',
    'tomato',
    'garlic',
    'eggs',
    'flour',
    'noodles'
]

print 'Welcome to the Inventory program！'

item = raw_input('What item do you want to check? ')

if item in inventory:
    print 'Yes, we have it'
else:
    print "No, we don't have it"
