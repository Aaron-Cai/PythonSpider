#coding: utf-8
#测试正则表达式

import re

pattern = re.compile(r'hello')

match1 = pattern.match('hello world!')
match2 = pattern.match('helloo world!')
match3 = pattern.match('helllo world!')

if match1:
	print match1.group()
else:
	print u'match1 匹配失败!'

if match2:
	print match2.group()
else:
	print u'match2 匹配失败!'

if match3:
	print match3.group()
else:
	print u'match3 匹配失败!'

