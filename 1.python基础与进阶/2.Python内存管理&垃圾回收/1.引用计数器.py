"""
1.环状双向链表 refchain
    Python程序中创建的任何对象都会放在refchain中
    name = 'penny'
    age = 23
    hobby = ['dog', 'cat']
    都会放在链表中

"""
# 1.1在内部会创建一些数据【上一个对象 下一个对象 类型 引用个数】
name = 'penny'
new = name

# 1.2在内部会创建一些数据【上一个对象 下一个对象 类型 引用个数 value = 23】
age = 23

# 1.3在内部会创建一些数据【上一个对象 下一个对象 类型 引用个数 items = 元素，元素个数】
hobby = ['dog', 'cat']

# 在C源码中如何体现每个对象都有相同的值：PyObject结构体（4个值）
# 有多个元素组成的对象，在PyObject结构体（4个值） + ob_size 。

"""
2.类型封装结构体
    float类型除了PyObject结构体（4个值） + ob_fval
        data = 3.14
        内部会创建: 
            _ob_next = refchain 中下一个对象
            _ob_prev = refchain 中上一个对象
            ob_refcnt = 1
            ob_type = float
            ob_fval = 3.14
"""
data = 3.14

"""
3.引用计数器
    v1 = 3.14
    v2 = 999
    v3 = (1,2,3,4)
    当Python程序运行时，会根据数据类型不同找对应的结构体，
    根据结构体中的字段创建相关的数据，将对象添加到refchain双线链表中
    
    在C源码中有两个关键的结构体：PyObject PyVarObject
    每个对象中都有ob_refcnt 就是引用计数器，当有其他变量引用对象，引用计数器会发生变化
"""
# 引用计数器加一
a = 9999
b = a

# 引用计数器减一
a = 9999
c = a
del c  # c变量被删除，c对应的对象引用计数器 -1
del a  # a 变量被删除，a对象引用计数器-1

# 引用计数器为零时，意味着没有人使用这个对象，需要进行垃圾回收
# 1.将对象从refchain链表中移除 2.将对象销毁，内存归还
