# encoding: utf-8
# module _pickle
# from /var/www/newsbytes/CPP/venv/lib/python3.6/site-packages/google/protobuf/pyext/_message.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
""" Optimized C implementation for the Python pickle module. """
# no imports

# functions

def dump(obj): # real signature unknown; restored from __doc__
    """
    Write a pickled representation of obj to the open file object file.
    
    This is equivalent to ``Pickler(file, protocol).dump(obj)``, but may
    be more efficient.
    
    The optional *protocol* argument tells the pickler to use the given
    protocol supported protocols are 0, 1, 2, 3 and 4.  The default
    protocol is 3; a backward-incompatible protocol designed for Python 3.
    
    Specifying a negative protocol version selects the highest protocol
    version supported.  The higher the protocol used, the more recent the
    version of Python needed to read the pickle produced.
    
    The *file* argument must have a write() method that accepts a single
    bytes argument.  It can thus be a file object opened for binary
    writing, an io.BytesIO instance, or any other custom object that meets
    this interface.
    
    If *fix_imports* is True and protocol is less than 3, pickle will try
    to map the new Python 3 names to the old module names used in Python
    2, so that the pickle data stream is readable with Python 2.
    """
    pass

def dumps(*args, **kwargs): # real signature unknown
    """
    Return the pickled representation of the object as a bytes object.
    
    The optional *protocol* argument tells the pickler to use the given
    protocol; supported protocols are 0, 1, 2, 3 and 4.  The default
    protocol is 3; a backward-incompatible protocol designed for Python 3.
    
    Specifying a negative protocol version selects the highest protocol
    version supported.  The higher the protocol used, the more recent the
    version of Python needed to read the pickle produced.
    
    If *fix_imports* is True and *protocol* is less than 3, pickle will
    try to map the new Python 3 names to the old module names used in
    Python 2, so that the pickle data stream is readable with Python 2.
    """
    pass

def load(): # real signature unknown; restored from __doc__
    """
    Read and return an object from the pickle data stored in a file.
    
    This is equivalent to ``Unpickler(file).load()``, but may be more
    efficient.
    
    The protocol version of the pickle is detected automatically, so no
    protocol argument is needed.  Bytes past the pickled object's
    representation are ignored.
    
    The argument *file* must have two methods, a read() method that takes
    an integer argument, and a readline() method that requires no
    arguments.  Both methods should return bytes.  Thus *file* can be a
    binary file object opened for reading, an io.BytesIO object, or any
    other custom object that meets this interface.
    
    Optional keyword arguments are *fix_imports*, *encoding* and *errors*,
    which are used to control compatibility support for pickle stream
    generated by Python 2.  If *fix_imports* is True, pickle will try to
    map the old Python 2 names to the new names used in Python 3.  The
    *encoding* and *errors* tell pickle how to decode 8-bit string
    instances pickled by Python 2; these default to 'ASCII' and 'strict',
    respectively.  The *encoding* can be 'bytes' to read these 8-bit
    string instances as bytes objects.
    """
    pass

def loads(*args, **kwargs): # real signature unknown
    """
    Read and return an object from the given pickle data.
    
    The protocol version of the pickle is detected automatically, so no
    protocol argument is needed.  Bytes past the pickled object's
    representation are ignored.
    
    Optional keyword arguments are *fix_imports*, *encoding* and *errors*,
    which are used to control compatibility support for pickle stream
    generated by Python 2.  If *fix_imports* is True, pickle will try to
    map the old Python 2 names to the new names used in Python 3.  The
    *encoding* and *errors* tell pickle how to decode 8-bit string
    instances pickled by Python 2; these default to 'ASCII' and 'strict',
    respectively.  The *encoding* can be 'bytes' to read these 8-bit
    string instances as bytes objects.
    """
    pass

# classes

class PickleError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Pickler(object):
    """
    This takes a binary file for writing a pickle data stream.
    
    The optional *protocol* argument tells the pickler to use the given
    protocol; supported protocols are 0, 1, 2, 3 and 4.  The default
    protocol is 3; a backward-incompatible protocol designed for Python 3.
    
    Specifying a negative protocol version selects the highest protocol
    version supported.  The higher the protocol used, the more recent the
    version of Python needed to read the pickle produced.
    
    The *file* argument must have a write() method that accepts a single
    bytes argument. It can thus be a file object opened for binary
    writing, an io.BytesIO instance, or any other custom object that meets
    this interface.
    
    If *fix_imports* is True and protocol is less than 3, pickle will try
    to map the new Python 3 names to the old module names used in Python
    2, so that the pickle data stream is readable with Python 2.
    """
    def clear_memo(self, *args, **kwargs): # real signature unknown
        """
        Clears the pickler's "memo".
        
        The memo is the data structure that remembers which objects the
        pickler has already seen, so that shared or recursive objects are
        pickled by reference and not by value.  This method is useful when
        re-using picklers.
        """
        pass

    def dump(self, *args, **kwargs): # real signature unknown
        """ Write a pickled representation of the given object to the open file. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
        pass

    bin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dispatch_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    memo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    persistent_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class PicklingError(PickleError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Unpickler(object):
    """
    This takes a binary file for reading a pickle data stream.
    
    The protocol version of the pickle is detected automatically, so no
    protocol argument is needed.  Bytes past the pickled object's
    representation are ignored.
    
    The argument *file* must have two methods, a read() method that takes
    an integer argument, and a readline() method that requires no
    arguments.  Both methods should return bytes.  Thus *file* can be a
    binary file object opened for reading, an io.BytesIO object, or any
    other custom object that meets this interface.
    
    Optional keyword arguments are *fix_imports*, *encoding* and *errors*,
    which are used to control compatibility support for pickle stream
    generated by Python 2.  If *fix_imports* is True, pickle will try to
    map the old Python 2 names to the new names used in Python 3.  The
    *encoding* and *errors* tell pickle how to decode 8-bit string
    instances pickled by Python 2; these default to 'ASCII' and 'strict',
    respectively.  The *encoding* can be 'bytes' to read these 8-bit
    string instances as bytes objects.
    """
    def find_class(self, *args, **kwargs): # real signature unknown
        """
        Return an object from a specified module.
        
        If necessary, the module will be imported. Subclasses may override
        this method (e.g. to restrict unpickling of arbitrary classes and
        functions).
        
        This method is called whenever a class or a function object is
        needed.  Both arguments passed are str objects.
        """
        pass

    def load(self, *args, **kwargs): # real signature unknown
        """
        Load a pickle.
        
        Read a pickled object representation from the open file object given
        in the constructor, and return the reconstituted object hierarchy
        specified therein.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
        pass

    memo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    persistent_load = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class UnpicklingError(PickleError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', 'module_repr': <staticmethod object at 0x7f7fe8be2048>, 'find_spec': <classmethod object at 0x7f7fe8be2080>, 'find_module': <classmethod object at 0x7f7fe8be20b8>, 'create_module': <classmethod object at 0x7f7fe8be20f0>, 'exec_module': <classmethod object at 0x7f7fe8be2128>, 'get_code': <classmethod object at 0x7f7fe8be2198>, 'get_source': <classmethod object at 0x7f7fe8be2208>, 'is_package': <classmethod object at 0x7f7fe8be2278>, 'load_module': <classmethod object at 0x7f7fe8be22b0>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_pickle', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

