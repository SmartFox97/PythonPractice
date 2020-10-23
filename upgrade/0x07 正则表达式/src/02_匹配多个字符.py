import re

"""
* 匹配前一个字符出现0次或者无限次，即可有可无
"""
_data = re.match("[A-Z][a-z]*", "MnnM")
_data2 = re.match("[A-Z][a-z]*", "Aabcdef")
print('示例1：', _data.group(), '示例2：', _data2.group())

print("===" * 10)
"""
+ 匹配前一个字符出现1次或者无限次，即至少有1次
"""
_data = re.match("t.+o", "two")
if _data:
    print(_data.group())
else:
    print("匹配失败")

print("===" * 10)
"""
? 匹配前一个字符出现1次或者0次，即要么有1次，要么没有
"""
_data = re.match("https?", "http")
_data2 = re.match("https?", "https")
if all([_data, _data2]):
    print('示例1：', _data.group(), '示例2：', _data2.group())
else:
    print("匹配失败")

print("===" * 10)
"""
{m} 匹配前一个字符出现m次
{m,n} 匹配前一个字符出现从m到n次
"""
_data = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
_data2 = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
print('示例1：', _data.group(), '示例2：', _data2.group())
