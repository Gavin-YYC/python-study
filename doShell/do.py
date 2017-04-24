# coding=utf-8

import os

path = './li.sh'


print os.popen( path, 'r' ).read()
