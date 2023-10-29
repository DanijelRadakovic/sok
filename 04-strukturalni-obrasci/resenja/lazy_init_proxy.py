from abc import ABC, abstractmethod
from time import sleep

class Service(ABC):
    @abstractmethod
    def play(self):
        pass

    @property
    @abstractmethod
    def resolution(self):
        pass

    @resolution.setter
    @abstractmethod
    def resolution(self, new_resolution):
        pass

class Video360(Service):
    def __init__(self):
        self.res = 360
        sleep(1)

    def play(self):
        print(f"Playing video at {self.res} resolution.")
        sleep(1)

    @property
    def resolution(self):
        return self.res

    @resolution.setter
    def resolution(self, new_resolution):
        if new_resolution != self.res:
            self.res = new_resolution

class Video720(Service):
    def __init__(self):
        self.res = 720
        sleep(1)

    def play(self):
        print(f"Playing video at {self.res} resolution.")
        sleep(1)

    @property
    def resolution(self):
        return self.res

    @resolution.setter
    def resolution(self, new_resolution):
        if new_resolution != self.res:
            self.res = new_resolution

class VideoHD(Service):
    def __init__(self):
        self.res = 1080
        sleep(1)

    def play(self):
        print(f"Playing video at {self.res} resolution.")
        sleep(1)

    @property
    def resolution(self):
        return self.res

    @resolution.setter
    def resolution(self, new_resolution):
        if new_resolution != self.res:
            self.res = new_resolution

class VideoProxy(Service):
    def __init__(self):
        self.delegate = None
        self.__resolution = 0

    @property
    def resolution(self):
        return self.__resolution

    @resolution.setter
    def resolution(self, new_resolution):
        if new_resolution != self.__resolution:
            self.__resolution = new_resolution
            self.delegate = None

    def play(self):
        if self.delegate is None:
            if self.__resolution == 360:
                self.delegate = Video360()
            elif self.__resolution == 720:
                self.delegate = Video720()
            elif self.__resolution == 1080:
                self.delegate = VideoHD()
            else:
                print("Unsupported resolution")
                return

        self.delegate.play()

def client(service: Service):
    resolutions = [360, 720, 1080]
    for i in range(100):
        service.resolution = resolutions[i % 3]
        service.play()

def main():
    service = VideoProxy()
    client(service)

if __name__ == "__main__":
    main()
