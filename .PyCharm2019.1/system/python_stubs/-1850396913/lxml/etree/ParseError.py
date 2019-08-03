# encoding: utf-8
# module lxml.etree
# from /var/www/newsbytes/CricketPlayerDataScrapper/venv/lib/python3.6/site-packages/lxml/etree.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .LxmlSyntaxError import LxmlSyntaxError

class ParseError(LxmlSyntaxError):
    """
    Syntax error while parsing an XML document.
    
        For compatibility with ElementTree 1.3 and later.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



