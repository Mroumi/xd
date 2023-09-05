import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1
    print("专注时间到！")

try:
    minutes = 1
    countdown(minutes)
except ValueError:
    print("请输入有效的分钟数")
