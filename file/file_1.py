# coding=utf-8

# 可以利用管道符来读取文件内容
# cat text.txt | python file_1.py
# cat text.txt 是把文件的内容写到了标准输出（sys.stdout）
# python file_1.py 运行python脚本，从标准输入读，然后把结果输出到标准输出
# 管道符（|）是将一个命令的标准输出和下一条命令的标准输入连在一起

import sys

# 从标准输入中读内容
# read()方法会返回文件字符串
text = sys.stdin.read()

print text

words = text.split()
wordcount = len( words )

print "Wordcount: ", wordcount

