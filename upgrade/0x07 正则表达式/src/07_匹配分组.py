import re

"""
匹配左右任意一个表达式
"""
# 水果列表
fruit_list = ["apple", "orange", "pear"]
# 遍历数据
for value in fruit_list:
    # |    匹配左右任意一个表达式
    match_obj = re.match("apple|pear", value)
    if match_obj:
        print("%s是我想要的" % match_obj.group())
    else:
        print("%s不是我要的" % value)

print("===" * 10)
"""
将括号中字符作为一个分组
"""
_data = re.match("(qq):([1-9]\d{4,10})", "qq:1537411234")
if _data:
    print("匹配到的数据：", _data.group(), "匹配到的第一分组：", _data.group(1), "匹配到的第二分组", _data.group(2))
else:
    print("匹配失败")

print("===" * 10)
"""
引用分组num匹配到的字符串
"""
_data = re.match("<[a-zA-Z1-6]+>.*</[a-zA-Z1-6]+>", "<html>kksk</html>")

if _data:
    print(_data.group())
else:
    print("匹配失败")

print("===" * 10)
"""
(?P<name>) 分组起别名
(?P=name)  引用别名为name分组匹配到的字符串
"""
_data = re.match("<(?P<html1>[a-zA-Z1-6]+)><(?P<html2>[a-zA-Z1-6]+)>.*</(?P=html2)></(?P=html1)>","<html><h1>www.smartfox.cc</h1></html>")
if _data:
    print(_data.group())
else:
    print("匹配失败")