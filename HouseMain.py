import threading
from DeviceC import *
from time import ctime,sleep



threads = []
t1 = threading.Thread(target=FanControl)
threads.append(t1)
t2 = threading.Thread(target=DataInHouse)
threads.append(t2)

if __name__ == '__main__':
	for t in threads:
		t.setDaemon(True)
		t.start()
	t.join()
	print("all over %s"%ctime())