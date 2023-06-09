# simple_packaging_demo


```
cat this_is_test/hello.py

import datetime

def say_something(msg):
    cur_time = datetime.datetime.now()
    print("Hello {}, current time is {}".format(msg, str(cur_time)))
```

install as a local dependency

`pip install -e .`


```
>python main.py
Hello XYZ. , current time is 2023-06-09 17:10:11.076567
```

Now you can continue to modify the local pacakge, e.g.,

```
cat this_is_test/hello.py

import datetime

def say_something(msg):
    cur_time = datetime.datetime.now()

    print("Hello {}, current time is {}".format(msg, str(cur_time)))
    print("I've been modified")

```
Change will be automatically updated to installation dir.
To see this, rerun
```
>python main.py
Hello XYZ. , current time is 2023-06-09 17:19:37.617674
I've been modified
```
