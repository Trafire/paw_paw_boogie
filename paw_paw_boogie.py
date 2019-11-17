from controller import dance_pad
from multiprocessing import Process, Manager
import time

def f(d):
    print(d)
    time.sleep(1)

if __name__ == '__main__':
    manager = Manager()
    d = manager.dict(dance_pad.key_map)

    p1 = Process(target=dance_pad.update_control_map, args=(d,))
    p2 = Process(target=f, args=(d,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()



