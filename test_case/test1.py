# coding=utf-8
total = 19 + 9.99 + 13.97 + 20 + 15.97 + 9.97 + 10 * 2
party = 8
print 'Receipt for your meal'
if party >= 8:
    total = total + total * .2
    print '小费'
print 'Total: ', total
print "Thanks you for dining with us today!"
