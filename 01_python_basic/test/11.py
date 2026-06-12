from threading import RLock,Thread

def fun1():
    for i in range(0,50):
        print(i)
def fun2():
    for i in range(50,100):
        print(i)

if __name__ == "__main__":
    t1 = Thread(target=fun1)
    t2 = Thread(target=fun2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()