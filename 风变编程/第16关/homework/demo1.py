# -*- coding: utf-8 -*-
import time
for t in range(1 * 60, 0, -1):
    info = '请专注任务，还要保持专注 ' + str(t) + ' 秒哦！'
    print(info)
    print("\b" * (len(info) * 2), end="", flush=True)
    time.sleep(1)