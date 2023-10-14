# It will import modules specified by 
# `__all__` attribute of some_package/__init__.py 
from some_package import *
from independent_module import add
# Import module and access to its objects by using `.`
import independent_module


if __name__ == "__main__":
    # Importing from independent module example
    print(add(1, 2))
    # Equivalent to the following
    print(independent_module.add(1, 2))
    
    # Importing from package with __all__ variable set example
    print(module1.function_a())
    print(module2.function_b())

    try:
        print(module3.function_c())
    except NameError:
        print("You need to explicitly import module3!")

    # Relative importing is inside module3
    from some_package import module3
    print(module3.relative_import())
