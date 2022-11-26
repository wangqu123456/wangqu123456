import os
import sys
import random as rd


__file_name = os.path.realpath(__file__)
__cur_path = os.path.dirname(__file_name)

def fun(ok):
    # import random
    a = rd.randint(0, 10)
    if ok:
        import random



if __name__ == "__main__":
    print __file_name
    print __cur_path

