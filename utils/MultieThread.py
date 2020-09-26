import _thread
import time

def print_time(context, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % (context, time.ctime(time.time()) ))


def timeChecker(func,delay = 0):
    if (time.time() - self.timeStamp) > delay:
        func()
    else:
        print('你的上一个动作还未完成')


