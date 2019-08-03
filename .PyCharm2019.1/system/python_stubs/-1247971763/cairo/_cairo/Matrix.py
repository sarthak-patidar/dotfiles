# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


from .object import object

class Matrix(object):
    # no doc
    @classmethod
    def init_rotate(cls, *args, **kwargs): # real signature unknown
        pass

    def invert(self, *args, **kwargs): # real signature unknown
        pass

    def multiply(self, *args, **kwargs): # real signature unknown
        pass

    def rotate(self, *args, **kwargs): # real signature unknown
        pass

    def scale(self, *args, **kwargs): # real signature unknown
        pass

    def transform_distance(self, *args, **kwargs): # real signature unknown
        pass

    def transform_point(self, *args, **kwargs): # real signature unknown
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
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

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    x0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """X translation component of the affine transformation"""

    xx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """xx component of the affine transformation"""

    xy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """xy component of the affine transformation"""

    y0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Y translation component of the affine transformation"""

    yx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """yx component of the affine transformation"""

    yy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """yy component of the affine transformation"""


    __hash__ = None


