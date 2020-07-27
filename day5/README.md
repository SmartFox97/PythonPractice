# Day5 函数进阶与强化 2020.07.22

------

# 0x00：组包和拆包

### 一、组包

+ = 右边有多个数据时，会自动包装成为元组

  ```python
  _data = 10, 20, 30
  print(_data, type(_data))
  ```

  输出结果

  ```
  (10, 20, 30) <class 'tuple'>
  ```

### 二、拆包

+ 如果 **变量数量 = 容器长度**, 容器中的元素会一一对应赋值给变量

+ 拆包时要注意，需要拆的数据的个数要与变量的个数相同，否则程序会异常

+ 除了对元组拆包之外，还可以对列表、字典等拆包

  ```python
  _data = (10, 20, 30)
  a, b, c = _data
  print(a, b, c)
  ```

  输出结果

  ```python
  10 20 30
  ```

### 三、应用场景

+ 使用组包与拆包交换俩个变量的值

  ```python
  a = 10
  b = 20
  a, b = b, a  # 先自动组包，后自动解包(拆包)
  
  # 原理
  _tuple = b, a
  a, b = _tuple
  ```

+ 函数返回多个值

  ```python
  def _test():
  	return 10, 20, 30
  
  _data = _test()
  print(_data, type(_data))
  a, b, c = _test()
  print(a, b, c)
  ```

  输出结果

  ```python
  (10, 20, 30) <class 'tuple'>
  10 20 30
  ```

-----

# 0x01：引用

### 一、什么是引用

+ **引用**：是一个变量或值的另一个名字，又称别名
  + 赋值本质：给右边的变量或值，起一个别名
+ 可以使用 `id函数` 查看变量的引用地址，**引用地址相等**，**说明指向同一个内存空间**
  + 每一次运行程序，每次地址都可能不一样

### 二、赋值原理

+ 赋值原理

  在Python中，变量的赋值过程与C、C++、Java均是不同的！这几种语言都是先定义一个变量，在内存中为变量创建一处内存空间；在赋值的时候，直接向其内存空间中写入数据，所以在这几种语言中，变量的内存地址是保持不变的；在这些语言里，变量是对内存及其地址的抽象。

  而在Python中，一切变量都是对象，变量的存储是采用的是引用的方式，其存储的是变量值所在的内存地址，而不是变量值本身；所以通俗来讲，变量相当于一个指针，为变量赋值相当于是将指针指向了这个值的内存空间。

  > 为了能够更加直观的观察Python的赋值原理，我们可以使用`id()`函数来查看变量的引用地址，观察各操作前后变量的变化。

+ 图解原理

  在Python创建a = 123时，其实解释器做了以下俩件事情：

  1. 在内存中创建123这个数值
  2. 在内存中创建名为a的变量，并将a变量指向数值123的内存空间地址

  在之后将变量a赋值给变量b的过程中，解释器就只是创建了b变量后，将b变量指向a变量指向的内存空间地址而已；

  ```python
  a = 123
  b = a
  print('123数值的内存地址：',id(123))
  print('a的地址：', id(a))
  print('b的地址：', id(b))
  ```

  输出结果

  ```shell
  123数值的内存地址： 140720002967008
  a的地址： 140720002967008
  b的地址： 140720002967008
  ```

![赋值原理](https://oss.smartfox.cc/2020/07/24/c54cf42e8f984.png)

### 三、可变类型和不可变类型

+ 可变类型：在存储空间中可以直接修改的数据类型
  + 列表 list
  + 字典 dict
  + 集合set
  
+ 不可变类型: 在存储空间中不可以直接修改的数据类型
  + 数值类型 int, bool, float
  + 字符串 str
  + 元组 tuple
  
+ 可变类型与不可变类型的区别

  + **不可变类型：**在地址不变的情况下，不可修改内容

  继续前面一节的栗子，变量a将值赋给了变量b，这个时候若是对b重新赋值，Python又会怎么做呢？

  ```python
  a = 123
  b = a
  print('123数值的内存地址：',id(123))
  print('修改前a的地址：', id(a))
  print('修改前b的地址：', id(b))
  
  print('=' * 30)
  b = 321
  print('321数值的内存地址：',id(321))
  print('修改后a的地址：', id(a))
  print('修改后b的地址：', id(b))
  ```

  输出结果

  ```shell
  123数值的内存地址： 140720002967008
  修改前a的地址： 140720002967008
  修改前b的地址： 140720002967008
  ==============================
  321数值的内存地址： 2890265721168
  修改后a的地址： 140720002967008
  修改后b的地址： 2890265721168
  ```

  从上面的执行可以发现，对b变量重新赋值，其实解释器做的是以下俩件事情：

  1. 由于变量b是数值类型，是不可变类型的，所以解释器会新申请一段内存来存储321这个数值
  2. 修改变量b指向的地址为数值321的内存空间地址

  

  ![修改赋值](https://oss.smartfox.cc/2020/07/24/501e104be08ac.png)

  + **可变类型：**在地址不变的情况下，可以修改内容

   ```python
  _list = [1, 2, 3, 4]
  print('_list的内容', _list, '_list的地址', id(_list))
  _list.append(5)
  print('添加元素后，_list的内容', _list, '添加元素后，_list的地址', id(_list))
  _list[2] = 2
  print('修改元素后，_list的内容', _list, '修改元素后，_list的地址', id(_list))
   ```

  输出结果

  ```shell
  _list的内容 [1, 2, 3, 4] _list的地址 2698168009664
  添加元素后，_list的内容 [1, 2, 3, 4, 5] 添加元素后，_list的地址 2698168009664
  修改元素后，_list的内容 [1, 2, 2, 4, 5] 修改元素后，_list的地址 2698168009664
  ```

  ![列表添加元素](https://oss.smartfox.cc/2020/07/24/c1e50648c5231.png)

  ![修改列表中的值](https://oss.smartfox.cc/2020/07/24/c1476b140ead5.png)

  可以看出，在可变类型的变量中，添加或修改值是不会改变内存地址的；

  但是细化的来看列表，它又不是一成不变的，在最后一次列表修改当中，我们将_list[2]的值修改为2，这时候解释器又在干什么呢？

  ```python
  _list = [1, 2, 3, 4, 5]
  print(_list)
  print('修改前', '_list[1]的内存地址', id(_list[1]),
        '2的内存地址', id(2), '3的内存地址', id(3), '_list[2]的内存地址', id(_list[2]))
  
  _list[2] = 2
  print(_list)
  print('修改后', '_list[1]的内存地址', id(_list[1]),
        '2的内存地址', id(2), '3的内存地址', id(3), '_list[2]的内存地址', id(_list[2]))
  ```

  输出结果

  ```shell
  [1, 2, 3, 4, 5]
  修改前 _list[1]的内存地址 140719819265728 2的内存地址 140719819265728 3的内存地址 140719819265760 _list[2]的内存地址 140719819265760
  [1, 2, 2, 4, 5]
  修改后 _list[1]的内存地址 140719819265728 2的内存地址 140719819265728 3的内存地址 140719819265760 _list[2]的内存地址 140719819265728
  ```

  ![列表值修改](https://oss.smartfox.cc/2020/07/24/a3e283a4a736b.png)

  从输出结果和流程图可以看出，修改列表容量内的值时，解释器只是修改了指定元素指向的数值内存空间地址；对于整体的容器`_list`是没有做任何改变的，出现改变的只有容器中`_list[2]`元素指向的内存地址。

### 四、Python函数传参是引用传递

+ 值传递与引用传递

  + **值传递：**在方法被调用时，实参通过形参把它的内容副本传入方法内部，此时形参接收到的内容是实参值的一个拷贝，因此在方法内对形参的任何操作，都仅仅是对这个副本的操作，不影响原始值的内容。
  + **引用传递：**”引用”也就是指向真实内容的地址值，在方法调用时，实参的地址通过方法调用被传递给相应的形参，在方法体内，形参和实参指向通愉快内存地址，对形参的操作会影响的真实内容。

+ Python函数传参是引用传递

  同理，我们用一个例子来简单说明：

  ```python
  def _test(_data):
      print('_data In Function = ', id(_data))
  
  
  a = 10
  print('_data Before Function = ', id(a))
  _test(a)
  print('_data After Function = ', id(a))
  ```

  输出结果

  ```shell
  _data Before Function =  140720313341888
  _data In Function =  140720313341888
  _data After Function =  140720313341888
  ```

  可以看出，Python在将参数传入函数中过程中采用的是引用传递的方式。

  **但是！这个时候又有人**~~(其实就是我自己)~~**会问了:**

  既然Python传参的方式是引用传递，那么在函数内修改变量的值时，为什么不会对传入的变量发生改变呢？

  ```python
  def test_num(_data: int):
      print('_data In Function = ', _data)
      _data = 100
      print('_data modify In Function = ', _data)
  
  
  _a = 50
  print('传入函数前', _a)
  test_num(_a)
  print('传入函数后', _a)
  ```

  输出结果

  ```shell
  传入函数前 50
  _data In Function =  50
  _data modify In Function =  100
  传入函数后 50
  ```

  从结果可以看出，在函数内发生修改的变量值并不会影响变量`_a`的值。

  其实，这是和Python独特的赋值原理有关的！在上面写着，Python变量的赋值，其实是对值的引用；给变量重新赋值其实只是修改了变量指向保存值的内存空间地址。如下所示：

  ```python
  def test_num(_data: int):
      print('_data In Function = ', _data, '地址：', id(_data))
      _data = 100
      print('_data modify In Function = ', _data, '地址：', id(_data))
  
  
  _a = 50
  print('传入函数前', _a, '地址：', id(_a))
  test_num(_a)
  print('传入函数后', _a, '地址：', id(_a))
  ```

  输出结果

  ```shell
  传入函数前 50 地址： 140720313343168
  _data In Function =  50 地址： 140720313343168
  _data modify In Function =  100 地址： 140720313344768
  传入函数后 50 地址： 140720313343168
  ```

  从这里的结果可以看出，实参`_a`被传入函数后，被形参`_data`接收，实参`_a`和形参`_data`同时指向数值`50`的地址，但是在函数中对`_data`重新赋值`100`时，仅仅只是更改了形参`_data`的指向，而不会影响到实参`_a`的指向。

  以上是**不可变类型**传参时的情况，但是当函数传参遇上**可变类型**的变量时，又是另一种情况了。

  ```python
  _list = [1, 2, 3]
  
  
  def test_list(_data: list):
      print('_data In Function = ', _data, id(_data))
      _data.append(4)
      print('_data modify In Function = ', _data, id(_data))
  
  
  print('修改前', _list, id(_list))
  test_list(_list)
  print('修改后', _list, id(_list))
  ```

  输出结果

  ```shell
  修改前 [1, 2, 3] 2486102033344
  _data In Function =  [1, 2, 3] 2486102033344
  _data modify In Function =  [1, 2, 3, 4] 2486102033344
  修改后 [1, 2, 3, 4] 2486102033344
  ```

  可以发现**可变类型**变量`_list`作为实参传给函数形参`_data`，当函数内形参`_data`发生修改时，在函数外的实参`_list`也发生了改变。

  ![传参](https://oss.smartfox.cc/2020/07/25/ffba6e8f24bb2.png)

  从图中可以直观的发现，**可变类型**变量在Python函数传参时，传进去的其实是一个装着一堆元素的“盒子”的内存地址；当“盒子”内元素发生改变时，也仅仅只是改变了盒子内元素变量的指向，形参`_data`和实参`_list`的指向依旧是这个“盒子”的地址，没有丝毫改变。所以**可变类型**变量若在函数内被修改，是会影响到函数外的值的。

-----

# 0x03：常用的函数姿势

### 一、range

+ range() 方法可创建一个整数列表对象，一般用在 for 循环中
  - range(开始位置, 结束位置，步长)
    - 和切片用法差不多

### 二、列表推导式

+ 列表推导式：快速生成列表元素的表达形式，通过for添加列表元素的简洁写法
+ 推导式基本格式： [计算公式 for 循环 if 判断]
+ 特点：
  - 每循环一次，将计算公式的结果添加到列表中
  - 计算公式可以使用遍历出的数据
  - for 遍历出的数据 必须满足 if 判断 才会使用计算公式生成元素

### 三、匿名函数

+ 匿名函数是简单普通函数的简洁写法
+ 定义的函数没有名字,这样的函数叫做**匿名函数**

匿名函数的语法结构：

```python
lambda [形参1], [形参2], ... : [单行表达式] 或 [函数调用]
```

+ 匿名函数中不能使用 **while 循环、for 循环**，只能编写单行的表达式，或函数调用
+ 匿名函数中返回结果**不需要使用 return**，表达式的运行结果就是返回结果
+ 匿名函数中也可以不返回结果。例如： `lambda : print('hello world')`

### 四、递归函数

+ 什么是递归函数

  + 如果 **一个函数在内部调用其本身**，这个函数就是 **递归函数**。
  + 递归函数一般会在特定情况下**不再调用函数本身**（一定要有出口），否则会导致到达最大递归次数, 程序报错

+ 通过递归函数实现阶乘

  ```python
  def func(n):
      if n == 1:
          return 1
      else:
          return func(n-1) * n
  ```

+ 递归的执行过程

  ![递归函数调用流程](https://oss.smartfox.cc/2020/07/22/74e9174630e43.png)

### 五、enumerate与del

+ enumerate的使用
  
  + 通过 for 配合 enumerate 遍历容器同时获取元素索引位置、元素
  
  ```python
  for _index, _value in enumerate(_list):
      print(f'索引：{_index},数值：{_value}')
  ```
  
+ 通过del删除列表元素
  
  + 通过del删除列表元素：`del 列表[索引]`