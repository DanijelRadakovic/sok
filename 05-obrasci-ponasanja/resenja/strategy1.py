from abc import ABC, abstractmethod

class Sort(ABC):
    @abstractmethod
    def sort(self, students_list):
        pass

class BubbleSort(Sort):
    def sort(self, students_list):
        print("BubbleSort")

class QuickSort(Sort):
    def sort(self, students_list):
        print("QuickSort")

class StudentskaSluzba:
    def __init__(self):
        self.sorter: Sort = BubbleSort()

    @property
    def sorter(self):
        return self._sorter

    @sorter.setter
    def sorter(self, new_sorter: Sort):
        self._sorter = new_sorter

    def show_students(self, students):
        self.sorter.sort(students)

def client():
    sluzba = StudentskaSluzba()
    students = ['Student1', 'Student3', 'Student2']

    sluzba.sorter = QuickSort()
    sluzba.show_students(students)

    sluzba.sorter = BubbleSort()
    sluzba.show_students(students)

if __name__ == "__main__":
    client()
