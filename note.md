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
>     for i inrange(stack.top, -1, -1):
>         if num == stack.data[i]:
>             stack.top = i - 1
>             return stack.data[i::-1]  # 错误：应该返回 stack.data[i:stack.top+2]
>     returnNone

> def compare_stack(num: int, stack: Stack) -> List:
>     original_top = stack.top
>     for i in range(stack.top, -1, -1):
>         if num == stack.data[i]:
>             # 获取要取走的牌（从i到栈顶的所有牌）
>             result = stack.data[i:original_top+1]
>             stack.top = i - 1  # 更新栈顶
>             return result
>     return None

### 2.4 链表

> head is None ：判断变量是否指向 None 对象
> 不是判断对象内容是否为空，而是判断是否有对象存在
>
> 即使对象的所有属性都是 None，只要对象本身存在，head is None 就是 False
