import imp
# import sys
# print("Name of module3.py: ", __name__)
# print("Here is the sys.path: ", sys.path)

# Relative importing example
# `.` means go one level up in the package hierarchy considering
# module __name__
from .module1 import function_a


def function_c() -> str:
    return "Hi from function C!"

def relative_import() -> str:
    return function_a()
