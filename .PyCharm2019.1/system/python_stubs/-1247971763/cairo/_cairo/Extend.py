# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class Extend(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    NONE = 0
    PAD = 3
    REFLECT = 2
    REPEAT = 1
    __map = {
        0: 'NONE',
        1: 'REPEAT',
        2: 'REFLECT',
        3: 'PAD',
    }


