import time
def yun():
    time_ = time.gmtime().tm_sec


    x = 0
    while x < 20:

        print x
        x+=1
        time.sleep(1)

    print time_-time.gmtime().tm_sec
yun()