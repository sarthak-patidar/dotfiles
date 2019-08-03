# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


from .object import object

class RectangleInt(object):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """height of the rectangle"""

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """width of the rectangle"""

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """X coordinate of the left side of the rectangle"""

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Y coordinate of the the top side of the rectangle"""


    __hash__ = None


