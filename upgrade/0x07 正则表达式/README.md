# 七、Python与正则表达式 2020.08.20

# 0x00：正则表达式

在实际开发过程中经常会有查找符合某些复杂规则的字符串的需要，比如:邮箱、图片地址、手机号码等，这时候想匹配或者查找符合某些规则的字符串就可以使用正则表达式了。

+ 概念

  **正则表达式就是记录文本规则的代码**

+ 样子

  `0\d{2}-\d{8} `这个就是一个正则表达式，表达的意思是匹配的是座机号码

+ 特点

  - 正则表达式的语法很令人头疼，可读性差
  - 正则表达式通用行很强，能够适用于很多编程语言



-----

# 0x01：re模块

在Python中需要通过正则表达式对字符串进行匹配的时候，可以使用一个 re 模块

```python
# 导入re模块
import re

# 使用match方法进行匹配操作
result = re.match(正则表达式,要匹配的字符串)

# 如果上一步匹配到数据的话，可以使用group方法来提取数据
result.group()
```

举个栗子

```python
import re

# 使用match方法进行匹配操作
result = re.match("smartfox","smartfox.cc")
# 获取匹配结果
info = result.group()
print(info)
```

输出结果

```shell
smartfox
```

------

# 0x02：匹配单个字符

| 代码 | 功能                                     |
| :--: | :--------------------------------------- |
|  .   | 匹配任意1个字符（除了\n）                |
| [ ]  | 匹配[ ]中列举的字符                      |
|  \d  | 匹配数字，即0-9                          |
|  \D  | 匹配非数字，即不是数字                   |
|  \s  | 匹配空白，即 空格，tab键                 |
|  \S  | 匹配非空白                               |
|  \w  | 匹配非特殊字符，即a-z、A-Z、0-9、_、汉字 |
|  \W  | 匹配特殊字符，即非字母、非数字、非汉字   |

+ 举个栗子

```python
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
```

输出结果

```shell
M
too
two
==============================
方法一： 7Hello Python 方法二： 7Hello Python
匹配A-Z： Hello Python 匹配a-z： hello Python 匹配A-Z，a-z: hello Python
==============================
匹配数字： hit:1 匹配非数字 f
匹配空白： hit:  匹配非空白 f
匹配非特殊字符： hit:1 匹配特殊字符 $
```

-------

# 0x03：匹配多个字符

| 代码  | 功能                                                |
| :---: | :-------------------------------------------------- |
|   *   | 匹配前一个字符出现0次或者无限次，即可有可无         |
|   +   | 匹配前一个字符出现1次或者无限次，即至少有1次        |
|   ?   | 匹配前一个字符出现1次或者0次，即要么有1次，要么没有 |
|  {m}  | 匹配前一个字符出现m次                               |
| {m,n} | 匹配前一个字符出现从m到n次                          |

+ 举个栗子

```python
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
```

输出结果

```shell
示例1： Mnn 示例2： Aabcdef
==============================
two
==============================
示例1： http 示例2： https
==============================
示例1： 12a3g4 示例2： 1ad12f23s34455ff66
```

------

# 0x04：匹配开头和结尾

|    代码     | 功能                   |
| :---------: | :--------------------- |
|      ^      | 匹配字符串开头         |
|      $      | 匹配字符串结尾         |
| [^指定字符] | 表示除了指定字符都匹配 |

+ 匹配以数字开头的数据

```python
import re

def check(data):
    if data:
        print(data.group())
    else:
        print("匹配失败")

# 匹配以数字开头的数据
_data = re.match("^\d.*", "3hello")
check(_data)
print("===" * 10)
_data = re.match("^\d.*", "ihello")
check(_data)
```

输出结果

```shell
3hello
==============================
匹配失败
```

+ 匹配以数字结尾的数据

```python
import re

def check(data):
    if data:
        print(data.group())
    else:
        print("匹配失败")

# 匹配以数字开头的数据
_data = re.match(".*\d$", "hello5")
check(_data)
print("===" * 10)
_data = re.match(".*\d$", "hellos")
check(_data)
```
输出结果

```shell
hello5
==============================
匹配失败
```

+ 匹配以数字开头和数字结尾的数据

```python
import re

def check(data):
    if data:
        print(data.group())
    else:
        print("匹配失败")

# 匹配以数字开头的数据
_data = re.match("^\d.*\d$", "4hello4")
check(_data)
print("===" * 10)
_data = re.match("^\d.*\d$", "hello4")
check(_data)
print("===" * 10)
_data = re.match("^\d.*\d$", "4hello")
check(_data)

```

输出结果

```shell
4hello4
==============================
匹配失败
==============================
匹配失败
```

+ 除了指定字符以外都匹配

```python
import re

def check(data):
    if data:
        print(data.group())
    else:
        print("匹配失败")

# 匹配以数字开头的数据
_data = re.match("[^aeiou]", "hello")
check(_data)
print("===" * 10)
_data = re.match("[^aeiou]", "all")
check(_data)
```

输出结果

```shell
h
==============================
匹配失败
```

------

# 0x05：匹配分组

|     代码     | 功能                             |
| :----------: | :------------------------------- |
|      \|      | 匹配左右任意一个表达式           |
|     (ab)     | 将括号中字符作为一个分组         |
|    `\num`    | 引用分组num匹配到的字符串        |
| `(?P<name>)` | 分组起别名                       |
|  (?P=name)   | 引用别名为name分组匹配到的字符串 |

+ 举个栗子

```python
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
```

输出结果

```shell
apple是我想要的
orange不是我要的
pear是我想要的
==============================
匹配到的数据： qq:1537411234 匹配到的第一分组： qq 匹配到的第二分组 1537411234
==============================
<html>kksk</html>
==============================
<html><h1>www.smartfox.cc</h1></html>
```



