import re

"""
匹配任意1个字符（除了\n）
"""
_data = re.match(".", "M")
print(_data.group())
_data = re.match("t.o", "too")
print(_data.group())
_data = re.match("t.o", "two")
print(_data.group())

print("===" * 10)
"""
匹配[ ]中列举的字符
"""
# 匹配0-9
_data = re.match("[0123456789]Hello Python", "7Hello Python")
_data2 = re.match("[0-9]Hello Python", "7Hello Python")
print("方法一：", _data.group(), "方法二：", _data2.group())
# 匹配A-Z,a-z
_data = re.match("[A-Z]ello Python", "Hello Python")
_data2 = re.match("[a-z]ello Python", "hello Python")
_data3 = re.match("[a-z,A-Z]ello Python", "hello Python")
print("匹配A-Z：", _data.group(), "匹配a-z：", _data2.group(),"匹配A-Z，a-z:",_data3.group())

print("===" * 10)
"""
\d 匹配数字，即0-9
\D 匹配非数字，即不是数字
\s 匹配空白，即 空格，tab键
\S 匹配非空白
\w 匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
\W 匹配特殊字符，即非字母、非数字、非汉字
"""

_data = re.match("hit:\d", "hit:1")
_data2 = re.match("\D", 'fox')
print("匹配数字：", _data.group(), "匹配非数字", _data2.group())
_data = re.match("hit:\s", "hit: ")
_data2 = re.match("\S", 'fox')
print("匹配空白：", _data.group(), "匹配非空白", _data2.group())
_data = re.match("hit:\w", "hit:1")
_data2 = re.match("\W", '$fox')
print("匹配非特殊字符：", _data.group(), "匹配特殊字符", _data2.group())
