# coding=utf-8

# 以正确的宽度在居中的“盒子”内打印一个句子

# 注意：整数除法运算符（\\）只能在python 2.2 以及后续版本，在之前的版本中，只使用普通除法（\）

sentence = raw_input("Sentence: ")

screen_width = 80

text_width = len( sentence )

box_width = text_width + 6

left_padding = 2
left_margin = ( screen_width - box_width ) // 2

print screen_width * '-'

print
print ' ' * left_margin + '+' + '-' * ( box_width - 2 ) + '+'
print ' ' * left_margin + '|' + ' ' * ( box_width - 2 ) + '|'
print ' ' * left_margin + '|' + ' ' * left_padding + sentence  + ' ' * left_padding + '|'
print ' ' * left_margin + '|' + ' ' * ( box_width - 2 ) + '|'
print ' ' * left_margin + '+' + '-' * ( box_width - 2 ) + '+'
print


