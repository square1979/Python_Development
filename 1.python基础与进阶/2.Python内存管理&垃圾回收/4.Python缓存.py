"""
1.池(int)：为了避免重复创建和销毁一些常见对象维护池
    启动解释器时，Python内部会创建-5 -4 ... ... 257
    v1 = 7  # 内部不会开辟内存，直接去池中获取
    v2 = 8  # 内部不会开辟内存，直接去池中获取
    v3 = 8  # 与v2的内存地址相同

2.free_list(float) :当一个对象的引用计数器为零时，按理应该回收，
但是内部不会进行回收而是将对象先添加到free_list中当缓存
以后再去创建对象不用重新开辟内存空间，而是直接使用free_list

3.字典维护的free_list列表可以存储80个dict对象

4.tuple元组，维护一个free_list 列表 但是规则不同
    free_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    数组中元素可以是链表且每个链表最多容纳2000元组对象，元组free_list数组存储数字时
    是按照元组可容纳的个数为索引找到free_list，并添加到链表中

5.str类型维护Unicode_latin1[256]链表，内存将所有ASCII码缓存起来，以后使用时候不再反复创建
"""
# 1.池(int)：为了避免重复创建和销毁一些常见对象维护池
v2 = 9
v3 = 9
print(id(v2), id(v3))

v4 = 999
v5 = 999
print(id(v4), id(v5))

# 2.free_list :当一个对象的引用计数器为零时，按理应该回收，
v1 = 2.13  # 开辟内存空间内部存储结构体中定义几个值，再存到refchain中
del v1  # refchain中移除，将对象添加到free_list 中，但是有数量限制（100个float），free_list满了则销毁

# 3.字典维护的free_list列表可以存储80个dict对象
v1 = {'name': 'jay'}
print(id(v1))
v2 = {'name': '佩奇'}
print(id(v2))

# 4.tuple元组，维护一个free_list 列表 但是规则不同[id 不同]
tuple1 = ("A", 99)
print(id(tuple1))
del tuple1
tuple2 = ("A", 999)
print(id(tuple2))

# 5.str类型维护Unicode_latin1[256]链表，内存将所有ASCII码缓存起来，以后使用时候不再反复创建[id 不同]
v1 = "A"
print(id(v1))
del v1
v2 = "a"
print(id(v2))
