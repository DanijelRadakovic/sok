import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

if __name__ == '__main__':
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(singleton1 is singleton2)  # This should print True
