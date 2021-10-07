# -*- coding: utf-8 -*-

import time

input("欢迎使用“时间管理器”！请按回车继续。")



while True:

    task_name = input('请输入任务名：')

    task_time = int(input('你觉得自己至少可以专注这个任务多少分钟？输入 N 分钟'))

    input('此次任务信息：\n我要完成的任务：%s\n我至少要专注：%d分钟\n按回车开始计时：' % (task_name, task_time))
    start = time.time()  # 开始计时

    start_time = time.strftime('%Y-%m-%d %H:%M:%S',
                               time.localtime(time.time()))  # 格式化日期

# for t in range(task_time*60,0,-1):  # 实际代码：分钟转成秒要乘60，用-1来倒计时。

    for t in range(task_time*60, 0, -1):
        info = '请专注任务，还要保持专注 ' + str(t) + ' 秒哦！'
        print(info)
        print("\b" * (len(info) * 2), end="", flush=True)
        time.sleep(1)

    print('你已经专注了 %d 分钟，很棒~再加把劲，完成任务！' % task_time)  # 倒计时后，才继续运行之后的代码。

    # 询问任务是否完成
    task_status = input('请在任务完成后按输入y:')
    if task_status == 'y':
        end = time.time()  # 一定用户按了 y，就记下结束时间。

        end_time = time.strftime('%Y-%m-%d %H:%M:%S',
                                 time.localtime(time.time()))  # 日期格式化
        actual_time = int((end - start) / 60)  # 始末时间相减，从秒换算到分，除以60。

        start_end = start_time + '——' + end_time + '\n'
        with open('timelog3.txt', 'a', encoding='utf-8') as f:
            str='从'+start_end+'之间我完成了任务：'+task_name+'\n'
            f.write(str)
        break
