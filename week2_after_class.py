# 1、编写一个函数输出乘法口诀表，执行结果如图所示（提示：print 默认输出后会换行，可以通过 print 参数控制是否换行）
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}'.format(i, j, i*j), end='\t')
    print()
################################ 
for i in range(1, 10):
    for j in range(1, i + 1):
        end_flag = '\n' if i == j else '\t'
        print(f'{i}*{j}={i*j}', end=end_flag)

# 2、编写一个函数遍历并打印 1 到 100，如果数字能被3整除，显示 Fizz；如果数字能被 5 整除，显示 Buzz；如果能同时被 3 和 5 整除，就显示 FizzBuzz
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

# 3、编写一个函数，输出 10 以内的斐波那契数列
""" 在数学上，费波那契数列是以递归的方法来定义：
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)（n≧2）

用文字来说，就是费波那契数列由0和1开始，之后的费波那契系数就是由之前的两数相加而得出。首几个费波那契系数是：
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
"""

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
for i in range(11):
    print(fib(i))
################################   
fib_cache = {0: 0, 1: 1}
def fibonacci(n):
    if n not in fib_cache:
        fib_cache[n] = fibonacci(n-2) + fibonacci(n-1)
    return fib_cache[n]
for i in range(11):
    print(fibonacci(i))    

# 4、完成课后阅读任务并提交阅读笔记
