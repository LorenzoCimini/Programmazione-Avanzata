import threading
import time
import functools




"""
    class threading.Thread(group=None, target=None, name=None, args=(), kwargs={})

    - Group     : Should be None
    - Target    : Rappresenta callable object invocato dal metodo run()
    - Name      : Thread name
"""


class myThread(threading.Thread):
    def __init__(self, target=None, args=()):
        self.fun = target
        self.result=None
        self.args=args
        super().__init__(target=self.exeFun, args=self.args)

    def exeFun(self, *args):
        self.result = self.fun(*args)
    
    def is_done(self):
        return not self.result==None
    
    def get_result(self):
        if self.is_done():
            return self.result
        else:
            raise "Non ancora pronto"


def asynchronous(f):
    def onCall(*args):
        th = myThread(target=f, args=args)
        th.start()
        return th
    return onCall

@asynchronous
def long_process(num):
    time.sleep(4)
    return num * num

res=None
result = long_process(12)
for i in range(6):
    time.sleep(1)
    if result.is_done():
        print("[{1}]: result {0}".format(result.get_result(), i))
    else: 
        print("[{0}]: not ready yet".format(i))




"""
    ------------ SLEEP SORT
"""


class myThread(threading.Thread):
    def __init__(self, target=None, args=()):
        super().__init__(target=self.myFun, args=args)

        """
            Nasceranno tutti thread in contemporanea ( lo scopo del threading e' proprio questo )
            e, di conseguenza, vado a stampare quello che finisce prima
            ovviamente finiranno prima quelli piu' piccoli perche' lo sleep
            lavora sul loro valore.
        """
    def myFun(self, *args):
        time.sleep(args[0]*0.1)
        print(str(args[0])+" ", end="")



"""
    Per ogni n in lista, creo un Thread con parametro [n]

    Avrò quindi una lista di thread

    ogni thread nella lista lo faccio partire
"""

def sleepsort(lst):
    ths=[myThread(args=[n]) for n in lst]
    for th in ths:
        th.start()

sleepsort([7, 2 ,100, 1, 9, 45, 2, 33, 7, 77, 25])




