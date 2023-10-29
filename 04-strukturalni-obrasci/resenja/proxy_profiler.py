from abc import ABC, abstractmethod
from time import perf_counter, sleep

class Service(ABC):
    @abstractmethod
    def video360(self):
        pass

    @abstractmethod
    def video720(self):
        pass

    @abstractmethod
    def videoHD(self):
        pass

class VideoService(Service):
    def __init__(self, name):
        self.name = name

    def video360(self):
        print(f"{self.name} - Video 360")
        sleep(0.1)  # Simulate video processing time

    def video720(self):
        print(f"{self.name} - Video 720")
        sleep(0.2)  # Simulate video processing time

    def videoHD(self):
        print(f"{self.name} - Video HD")
        sleep(0.3)  # Simulate video processing time

class ProxyVS(Service):
    def __init__(self):
        self.real_service = VideoService("Real Service")
        self.call_stats = {
            "video360": {"calls": 0, "total_time": 0},
            "video720": {"calls": 0, "total_time": 0},
            "videoHD": {"calls": 0, "total_time": 0},
        }

    def video360(self):
        start_time = perf_counter()
        self.call_stats["video360"]["calls"] += 1
        self.real_service.video360()
        end_time = perf_counter()
        execution_time = end_time - start_time
        self.call_stats["video360"]["total_time"] += execution_time

    def video720(self):
        start_time = perf_counter()
        self.call_stats["video720"]["calls"] += 1
        self.real_service.video720()
        end_time = perf_counter()
        execution_time = end_time - start_time
        self.call_stats["video720"]["total_time"] += execution_time

    def videoHD(self):
        start_time = perf_counter()
        self.call_stats["videoHD"]["calls"] += 1
        self.real_service.videoHD()
        end_time = perf_counter()
        execution_time = end_time - start_time
        self.call_stats["videoHD"]["total_time"] += execution_time

    def show_stats(self):
        for method, stats in self.call_stats.items():
            print(f"Method: {method}")
            print(f"Total Calls: {stats['calls']}")
            print(f"Total Execution Time: {stats['total_time']:.4f} seconds")
            if stats['calls'] > 0:
                average_time_per_call = stats['total_time'] / stats['calls']
                print(f"Average Execution Time per Call: {average_time_per_call:.4f} seconds")
            print()

def client(service: Service):
    for i in range(100):
        service.video360()
        service.video720()
        service.videoHD()

def main():
    service = ProxyVS()
    client(service)
    service.show_stats()

if __name__ == "__main__":
    main()
