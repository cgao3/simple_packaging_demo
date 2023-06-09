import datetime

def say_something(msg):
    cur_time = datetime.datetime.now()
    print("Hello {}, current time is {}".format(msg, str(cur_time)))
