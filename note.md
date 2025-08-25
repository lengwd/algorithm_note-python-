# 算法笔记-python版

> 来自《啊哈！算法》
>
> 书中是C的算法 笔者常用的是python 所以提交了这个版本 并且 写了一些遇到的问题

## 一、排序算法

### 1.1 桶排序

> python如何创建全零：
>
> * 简单需求：`[0] * n`
> * 数值计算：`numpy.zeros()`
> * 需要后续修改：列表推导式 `[0 for _ in range(n)]`

> 如何反向排序：
>
> # 从大到小：range(start, stop, step)
>
> for i in range(m-1, -1, -1):

### 1.2 冒泡排序

> 没有遇到问题

### 1.3 快速排序

> 递归算法集的边界设置清楚
>
> 错误： temp=nums[0]
>
> 正确：temp=nums[left]

## 二、队列、栈、链表

### 2.3 小猫钓鱼

> s.top = -1# 空栈状态

compare_stack 函数返回值错误

> defcompare_stack(num: int, stack: Stack) -> List:
> for i inrange(stack.top, -1, -1):
> if num == stack.data[i]:
> stack.top = i - 1
> return stack.data[i::-1]  # 错误：应该返回 stack.data[i:stack.top+2]
> returnNone

> def compare_stack(num: int, stack: Stack) -> List:
> original_top = stack.top
> for i in range(stack.top, -1, -1):
> if num == stack.data[i]:
>
> # 获取要取走的牌（从i到栈顶的所有牌）
>
> result = stack.data[i:original_top+1]
> stack.top = i - 1  # 更新栈顶
> return result
> return None

### 2.4 链表

> head is None ：判断变量是否指向 None 对象
> 不是判断对象内容是否为空，而是判断是否有对象存在
>
> 即使对象的所有属性都是 None，只要对象本身存在，head is None 就是 False

## 三、universal search

这一章是这本书核心的部分

### 3.1 depth-first search

深度优先搜索 即优先探索一条路到底 再依次返回

整体结构：

> 函数：
>
> 返回条件
>
> 当前操作 （其中包含调用函数本身的下一步）
>
> 撤回当前操作 （这一步是返回的必要条件）

技巧1：

> book 用于记录，常常用于不可重复使用的数字序列之类的

知识补充：LEGB规则

> # G - Global 全局变量
>
> global_var = "I'm global"
>
> # B - Built-in 内置函数（如print, len等）
>
> def outer_function():
>
> # E - Enclosing 外层函数变量
>
> enclosing_var = "I'm enclosing"
>
> def inner_function():
>
> # L - Local 局部变量
>
> local_var = "I'm local"
>
> # 按LEGB顺序查找
>
> print(f"Local: {local_var}")           # L - 找到
>
> print(f"Enclosing: {enclosing_var}")   # E - 向外查找
>
> print(f"Global: {global_var}")         # G - 继续向外查找
>
> print(f"Built-in: {len('hello')}")     # B - 内置函数
>
> inner_function()
>
> outer_function()

> 案例1：
>
> def outer():
> count = 0
>
> def inner():
> count += 1  # 错误！UnboundLocalError
> print(count)
>
> inner()
>
> outer()
>
> 在这个例子中 count += 1是个赋值操作 被认为是 局部变量
>
> 但是没有初始值报错

### 3.2 解救小哈

知识点1

> 定义无穷大：min_steps=float("inf") 没有int("inf")

知识点2：

> # 错误的写法
>
> book = [[0] * n] * m  # 这会创建m个指向同一个列表的引用！
>
> # 正确的写法
>
> book = [[0] * n for _ in range(m)]
>
> # 错误示例
>
> book = [[0] * 3] * 2
>
> book[0][0] = 1
>
> print(book)  # 输出: [[1, 0, 0], [1, 0, 0]] - 两行都被修改了

初始化问题

> book[x_init][y_init] = 1
>
> # min_steps应该初始化为0，而不是作为step参数传递
>
> dfs(x_init, y_init, min_steps)  # 错误
>
> dfs(x_init, y_init, 0)         # 正确

### 3.3 广度优先算法

错误1：

> out of index
>
> 原因：没有标记已经走过的路

技巧1：

> 在while的判断条件上加上 not found

### 3.4 本章小结

这两个搜索算法让我初步体会算法的有趣 主要是一种决策的思维

深度优先 和 广度优先

深度优先 主要是用递归实现，如果是搜索记得去除 标记 ，

主题结构：

返回条件

越界

规则

调用

去除标记（如果是计数的类别 不需要去除 如 05）

广度优先主要利用的是队列

结构

初始化

while head < tail

越界

规则

比较有意思
