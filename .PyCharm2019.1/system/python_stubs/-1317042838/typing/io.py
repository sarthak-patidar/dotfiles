# encoding: utf-8
# module typing.io
# from /var/www/newsbytes/CPP/venv/lib/python3.6/site-packages/pandas/util/_move.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
""" Wrapper namespace for IO generic classes. """

# imports
import typing as __typing


# no functions
# classes

class IO(__typing.Generic):
    """
    Generic base class for TextIO and BinaryIO.
    
        This is an abstract, generic version of the return of open().
    
        NOTE: This does not distinguish between the different possible
        classes (text vs. binary, read vs. write vs. read/write,
        append-only, unbuffered).  The TextIO and BinaryIO subclasses
        below capture the distinctions between text vs. binary, which is
        pervasive in the interface; however we currently do not offer a
        way to track the other distinctions in the type system.
    """
# Error generating skeleton for function close: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function closed: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function fileno: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function flush: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function isatty: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function read: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function readable: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function readline: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function readlines: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function seek: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function seekable: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function tell: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function truncate: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function writable: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function write: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function writelines: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function __enter__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function __exit__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _abc_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fa3138b20f0>'
    _abc_generic_negative_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fa3138b22e8>'
    _abc_generic_negative_cache_version = 44
    _abc_registry = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fa3138b20b8>'
    _gorg = typing.IO # (!) forward: IO, real value is 'typing.IO'
    __abstractmethods__ = frozenset({'isatty', 'fileno', 'tell', '__enter__', 'seek', 'truncate', 'close', '__exit__', 'readline', 'name', 'readable', 'closed', 'writelines', 'flush', 'seekable', 'read', 'write', 'mode', 'readlines', 'writable'})
    __args__ = None
    __extra__ = None
    __next_in_mro__ = object
    __origin__ = None
    __orig_bases__ = (
        typing.Generic[~AnyStr],
    )
    __parameters__ = (
        None, # (!) real value is '~AnyStr'
    )
    __slots__ = ()
    __tree_hash__ = -9223372036852454792


class BinaryIO(__typing.IO):
    """ Typed version of the return of open() in binary mode. """
# Error generating skeleton for function write: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

# Error generating skeleton for function __enter__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _abc_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fa3138b2550>'
    _abc_generic_negative_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fa3138b2588>'
    _abc_generic_negative_cache_version = 44
    _abc_registry = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fa3138b2518>'
    _gorg = typing.BinaryIO # (!) forward: BinaryIO, real value is 'typing.BinaryIO'
    __abstractmethods__ = frozenset({'isatty', 'tell', 'fileno', '__enter__', 'seek', 'truncate', 'close', '__exit__', 'readline', 'name', 'readable', 'closed', 'writelines', 'flush', 'writable', 'seekable', 'write', 'mode', 'readlines', 'read'})
    __args__ = None
    __extra__ = None
    __next_in_mro__ = object
    __origin__ = None
    __orig_bases__ = (
        typing.IO[bytes],
    )
    __parameters__ = ()
    __slots__ = ()
    __tree_hash__ = -9223372036852454932


class TextIO(__typing.IO):
    """ Typed version of the return of open() in text mode. """
# Error generating skeleton for function __enter__: Function has keyword-only parameters or annotations, use getfullargspec() API which can support them

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    line_buffering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    newlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _abc_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fa3138b27b8>'
    _abc_generic_negative_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fa3138b27f0>'
    _abc_generic_negative_cache_version = 44
    _abc_registry = None # (!) real value is '<_weakrefset.WeakSet object at 0x7fa3138b2780>'
    _gorg = typing.TextIO # (!) forward: TextIO, real value is 'typing.TextIO'
    __abstractmethods__ = frozenset({'isatty', 'line_buffering', 'fileno', 'tell', 'newlines', 'encoding', '__enter__', 'seek', 'truncate', 'close', '__exit__', 'readline', 'name', 'errors', 'readable', 'buffer', 'closed', 'writelines', 'flush', 'seekable', 'read', 'write', 'mode', 'readlines', 'writable'})
    __args__ = None
    __extra__ = None
    __next_in_mro__ = object
    __origin__ = None
    __orig_bases__ = (
        typing.IO[str],
    )
    __parameters__ = ()
    __slots__ = ()
    __tree_hash__ = -9223372036852454210


# variables with complex values

__all__ = [
    'IO',
    'TextIO',
    'BinaryIO',
]

__weakref__ = None # (!) real value is "<attribute '__weakref__' of 'typing.io' objects>"

