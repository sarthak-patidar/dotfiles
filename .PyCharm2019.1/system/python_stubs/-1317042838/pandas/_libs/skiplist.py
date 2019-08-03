# encoding: utf-8
# module pandas._libs.skiplist
# from /var/www/newsbytes/CPP/venv/lib/python3.6/site-packages/pandas/_libs/skiplist.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /var/www/newsbytes/CPP/venv/lib/python3.6/site-packages/numpy/__init__.py

# functions

def random(): # real signature unknown; restored from __doc__
    """ random() -> x in the interval [0, 1). """
    pass

def __pyx_unpickle_IndexableSkiplist(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Node(*args, **kwargs): # real signature unknown
    pass

# classes

class IndexableSkiplist(object):
    """
    Sorted collection supporting O(lg n) insertion, removal, and
        lookup by rank.
    """
    def get(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f1837bf7b40>'


class Node(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

NIL = None # (!) real value is '<pandas._libs.skiplist.Node object at 0x7f1837c0ae08>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f1837c0fef0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.skiplist', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f1837c0fef0>, origin='/var/www/newsbytes/CPP/venv/lib/python3.6/site-packages/pandas/_libs/skiplist.cpython-36m-x86_64-linux-gnu.so')"

__test__ = {}

