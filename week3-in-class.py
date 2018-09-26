# !/usr/bin/env python
# encoding: utf-8
"""
 
Created by aurorang on 2018/9/26.
Copyright (c) 2018 www.aurorawu.com All rights reserved.
"""


# 1、写一个函数：获取用户输入的名字（name）和年龄（age），计算一下该用户到哪一年（返回值）为100岁，并打印结果”{用户名字}在XXXX年为100岁”
def get_year_of_hundred():
    name = input('请输入您的名字：')
    age = int(input('请输入您当前的年龄：'))
    which_year = 100 + 2018 - age
    print(f'{name} 在 {which_year} 年为 100 岁')
    return which_year


get_year_of_hundred()


# 2、写一个函数：获取用户输入的整数，如果它是奇数则打印”您输入的是奇数”，如果是偶数则打印”您输入的是偶数”
def is_odd_or_even():
    number = int(input("请输入一个整数："))
    if number % 2 == 1:
        print("您输入的是奇数")
    else:
        print("您输入的是偶数")


is_odd_or_even()


# 3、写一个函数：输入参数是一个 list，判断该 list 中是否有空对象（至少用三种方法实现）
def has_null_value(lst):
    flag = True  # flag 为 True 时表示列表中有空对象
    for x in lst:
        if not bool(x):
            break
    else:
        flag = False  # 表示列表中没有空对象
    return flag


#################################################
def has_null_value(lst):
    return list(filter(None, lst)) == lst


#################################################
def has_null_value(lst):
    return all(lst)


has_null_value(['', 0.0, 4, 'hello'])
has_null_value([2.0, 4, 'hello'])


# 4、写一个函数：输入参数是一个整数列表，把该列表中每个整数都平方后返回新的列表（至少用两种方法实现）
def square(lst):
    return [x ** 2 for x in lst]


#################################
def square(lst):
    return list(map(lambda x: x ** 2, lst))


square([1, 2, 3])


# 5、写一个函数：输入参数是一个整数列表，使用 reduce 函数实现求和后返回结果
def my_sum(lst):
    from functools import reduce
    return reduce(lambda x, y: x + y, lst)


my_sum([1, 2, 3, 4])


# 6、写一个函数：请用列表推导式实现立方
def triple(lst):
    return [x ** 3 for x in lst]


triple([1, 2, 3])


# 7、写一个函数：输入参数是两个 list，请返回它们的共同元素所组成的新列表
def elements_in_common(m, n):
    s = set(m) & set(n)
    return list(s)


elements_in_common([1, 2, 3], [2, 3, 4])


# 8、写一个函数：找出三个整数中的最大数（至少用两种方法实现）
def max_in_three(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z


#################################
def max_in_three(x, y, z):
    from functools import reduce
    return reduce(lambda x, y: x if x > y else y, (x, y, z))
