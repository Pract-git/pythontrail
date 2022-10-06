from turtledemo.chaos import f

import foo

print ("before foo2function")


def foo2_func():
    print("Inside foo2 function")


if __name__ == '__main__':
    foo2_func()
    #print(f'hi {(foo.first_foo())}')
    print("finishing foo2")
