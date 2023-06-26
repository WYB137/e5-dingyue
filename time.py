import time

def auto_focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print("剩余时间：{} 秒".format(seconds))
        time.sleep(1)  # 暂停 1 秒
        seconds -= 1
    print("专注时间结束！")

focus_minutes = 3  # 设置专注时间为3分钟

auto_focus_timer(focus_minutes)
