from controller import dance_pad
from view import view
from model import model
from multiprocessing import Process, Manager
import time




if __name__ == '__main__':
    manager = Manager()
    controller_map = manager.dict(model.key_map)
    print("start")
    p1 = Process(target=dance_pad.update_control_map, args=(controller_map,))
    p2 = Process(target=view.display, args=(controller_map,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
