import threading
import time

THRESHOLD = 1000000


def calculate(i):
    start = THRESHOLD * i + 1
    end = THRESHOLD * (i + 1) + 1
    result = sum(range(start, end))
    print(threading.current_thread().name, result)
    return result


def test_demo1():
    # for i in range(10):
    #     calculate(i)
    t = []
    for i in range(10):
        x = threading.Thread(target=calculate, args=(i,))
        t.append(x)
        x.setDaemon(False)
        x.start()
    for y in t:
        y.join()
    print("end")


def test_demo2():
    a = [1, 2, 3]
    print("----")
    print(a[-1])
