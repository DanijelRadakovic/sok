from abc import ABC, abstractmethod


class Student:
    def __init__(self, broj_indeksa: int, ime: str, prezime: str):
        self.brojIndeksa = broj_indeksa
        self.ime = ime
        self.prezime = prezime


class StudentSelectionSort(ABC):
    @abstractmethod
    def compare(self, student1: Student, student2: Student) -> int:
        pass

    def sort(self, students_list):
        n = len(students_list)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if self.compare(students_list[j], students_list[min_idx]) == -1:
                    min_idx = j
            students_list[i], students_list[min_idx] = students_list[min_idx], students_list[i]


class StudentSortIndeks(StudentSelectionSort):
    def compare(self, student1: Student, student2: Student) -> int:
        if student1.brojIndeksa < student2.brojIndeksa:
            return -1
        elif student1.brojIndeksa > student2.brojIndeksa:
            return 1
        else:
            return 0


class StudentSortIme(StudentSelectionSort):
    def compare(self, student1: Student, student2: Student) -> int:
        if student1.ime.lower() < student2.ime.lower():
            return -1
        elif student1.ime.lower() > student2.ime.lower():
            return 1
        else:
            return 0


class StudentSortPrezime(StudentSelectionSort):
    def compare(self, student1: Student, student2: Student) -> int:
        if student1.prezime.lower() < student2.prezime.lower():
            return -1
        elif student1.prezime.lower() > student2.prezime.lower():
            return 1
        else:
            return 0


def client():
    students = [
        Student(2, "John", "Smith"),
        Student(1, "Alice", "Johnson"),
        Student(3, "Bob", "Brown")
    ]

    indeks_sort = StudentSortIndeks()
    ime_sort = StudentSortIme()
    prezime_sort = StudentSortPrezime()

    indeks_sort.sort(students)
    print("Sortirani po broju indeksa:")
    print(f"{student.brojIndeksa}: {student.ime} {student.prezime}" for student in students)

    ime_sort.sort(students)
    print("\nSortirani po imenu:")
    print(f"{student.brojIndeksa}: {student.ime} {student.prezime}" for student in students)

    prezime_sort.sort(students)
    print("\nSortirani po prezimenu:")
    print(f"{student.brojIndeksa}: {student.ime} {student.prezime}" for student in students)


if __name__ == "__main__":
    client()
