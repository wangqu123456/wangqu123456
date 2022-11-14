import os
import sys

__file_name = os.path.realpath(__file__)
__cur_path = os.path.dirname(__file_name)


if __name__ == "__main__":
    print __file_name
    print __cur_path

