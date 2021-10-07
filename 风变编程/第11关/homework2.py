# -*- coding: utf-8 -*-
print('\n欢迎使用除法计算器！\n')
while True:
    try:
        x = input('请你输入除数：')

        y = input('请你输入被除数：')

        z = float(x) / float(y)

        print(x, '/', y, '=', z)
        break  # 默认每次只计算一次，所以在这里写了 break。

    except ZeroDivisionError:
        print('0是不能做除数的！')

    except ValueError:
        print('除数和被除数都应该是整值或浮点数！')

# 方式2：将两个（或多个）异常放在一起，只要触发其中一个，就执行所包含的代码。
# except(ZeroDivisionError,ValueError):
#     print('你的输入有误，请重新输入！')

# 方式3：常规错误的基类，假设不想提供很精细的提示，可以用这个语句响应常规错误。

# except Exception:

#     print('你的输入有误，请重新输入！')