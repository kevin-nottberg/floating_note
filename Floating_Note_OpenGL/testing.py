from simple_vector_library import *

def main():
    position = Py_Vector(1, 0)
    velocity = Py_Vector(1, 0)

    #Add testing
    position.add(velocity)

    position.add([1, 0])

    position.add(1, 2)

main()
