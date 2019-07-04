#coding:utf-8
import threading
class Singleton(object):

    def __new__(cls, *args, **kwargs):
        lock = threading.Lock()
        lock.acquire()
        if not hasattr(cls, "_instance"):
            cls._instance = object.__new__(cls)
            cls._instance.__Singleton_Init__(*args, **kwargs)
        lock.release()
        return cls._instance

    def __Singleton_Init__(self):
        raise RuntimeError("__Singleton_Init__ must be overwritten")