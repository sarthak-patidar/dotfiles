# encoding: utf-8
# module lxml.html.diff
# from /home/sarthak/Programming/CricketPlayerDataScrapper/venv/lib/python3.6/site-packages/lxml/html/diff.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import difflib as difflib # /usr/lib/python3.6/difflib.py
import lxml.etree as etree # /home/sarthak/Programming/CricketPlayerDataScrapper/venv/lib/python3.6/site-packages/lxml/etree.cpython-36m-x86_64-linux-gnu.so
import re as re # /usr/lib/python3.6/re.py
import difflib as __difflib


# functions

def cleanup_delete(*args, **kwargs): # real signature unknown
    """
    Cleans up any DEL_START/DEL_END markers in the document, replacing
        them with <del></del>.  To do this while keeping the document
        valid, it may need to drop some tags (either start or end tags).
    
        It may also move the del into adjacent tags to try to move it to a
        similar location where it was originally located (e.g., moving a
        delete into preceding <div> tag, if the del looks like (DEL_START,
        'Text</div>', DEL_END)
    """
    pass

def cleanup_html(*args, **kwargs): # real signature unknown
    """
    This 'cleans' the HTML, meaning that any page structure is removed
        (only the contents of <body> are used, if there is any <body).
        Also <ins> and <del> tags are removed.
    """
    pass

def compress_merge_back(*args, **kwargs): # real signature unknown
    """
    Merge tok into the last element of tokens (modifying the list of
        tokens in-place).
    """
    pass

def compress_tokens(*args, **kwargs): # real signature unknown
    """
    Combine adjacent tokens when there is no HTML between the tokens, 
        and they share an annotation
    """
    pass

def copy_annotations(*args, **kwargs): # real signature unknown
    """ Copy annotations from the tokens listed in src to the tokens in dest """
    pass

def default_markup(*args, **kwargs): # real signature unknown
    pass

def end_tag(*args, **kwargs): # real signature unknown
    """
    The text representation of an end tag for a tag.  Includes
        trailing whitespace when appropriate.
    """
    pass

def expand_tokens(*args, **kwargs): # real signature unknown
    """
    Given a list of tokens, return a generator of the chunks of
        text for the data in the tokens.
    """
    pass

def fixup_chunks(*args, **kwargs): # real signature unknown
    """ This function takes a list of chunks and produces a list of tokens. """
    pass

def fixup_ins_del_tags(*args, **kwargs): # real signature unknown
    """
    Given an html string, move any <ins> or <del> tags inside of any
        block-level elements, e.g. transform <ins><p>word</p></ins> to
        <p><ins>word</ins></p>
    """
    pass

def flatten_el(*args, **kwargs): # real signature unknown
    """
    Takes an lxml element el, and generates all the text chunks for
        that tag.  Each start tag is a chunk, each word is a chunk, and each
        end tag is a chunk.
    
        If skip_tag is true, then the outermost container tag is
        not returned (just its contents).
    """
    pass

def fragment_fromstring(html, create_parent=False, base_url=None, parser=None, **kw): # reliably restored by inspect
    """
    Parses a single HTML element; it is an error if there is more than
        one element, or if anything but whitespace precedes or follows the
        element.
    
        If ``create_parent`` is true (or is a tag name) then a parent node
        will be created to encapsulate the HTML in a single element.  In this
        case, leading or trailing text is also allowed, as are multiple elements
        as result of the parsing.
    
        Passing a ``base_url`` will set the document's ``base_url`` attribute
        (and the tree's docinfo.URL).
    """
    pass

def htmldiff(*args, **kwargs): # real signature unknown
    """
    Do a diff of the old and new document.  The documents are HTML
        *fragments* (str/UTF8 or unicode), they are not complete documents
        (i.e., no <html> tag).
    
        Returns HTML with <ins> and <del> tags added around the
        appropriate text.  
    
        Markup is generally ignored, with the markup from new_html
        preserved, and possibly some markup from old_html (though it is
        considered acceptable to lose some of the old markup).  Only the
        words in the HTML are diffed.  The exception is <img> tags, which
        are treated like words, and the href attribute of <a> tags, which
        are noted inside the tag itself when there are changes.
    """
    pass

def htmldiff_tokens(*args, **kwargs): # real signature unknown
    """
    Does a diff on the tokens themselves, returning a list of text
        chunks (not tokens).
    """
    pass

def html_annotate(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    doclist should be ordered from oldest to newest, like::
    
            >>> version1 = 'Hello World'
            >>> version2 = 'Goodbye World'
            >>> print(html_annotate([(version1, 'version 1'),
            ...                      (version2, 'version 2')]))
            <span title="version 2">Goodbye</span> <span title="version 1">World</span>
    
        The documents must be *fragments* (str/UTF8 or unicode), not
        complete documents
    
        The markup argument is a function to markup the spans of words.
        This function is called like markup('Hello', 'version 2'), and
        returns HTML.  The first argument is text and never includes any
        markup.  The default uses a span with a title:
    
            >>> print(default_markup('Some Text', 'by Joe'))
            <span title="by Joe">Some Text</span>
    """
    pass

def html_annotate_merge_annotations(*args, **kwargs): # real signature unknown
    """
    Merge the annotations from tokens_old into tokens_new, when the
        tokens in the new document already existed in the old document.
    """
    pass

def html_escape(s, quote=True): # reliably restored by inspect
    """
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
        If the optional flag quote is true (the default), the quotation mark
        characters, both double quote (") and single quote (') characters are also
        translated.
    """
    pass

def is_end_tag(*args, **kwargs): # real signature unknown
    pass

def is_start_tag(*args, **kwargs): # real signature unknown
    pass

def is_word(*args, **kwargs): # real signature unknown
    pass

def locate_unbalanced_end(*args, **kwargs): # real signature unknown
    """
    like locate_unbalanced_start, except handling end tags and
        possibly moving the point earlier in the document.
    """
    pass

def locate_unbalanced_start(unbalanced_start, pre, post): # real signature unknown; restored from __doc__
    """
    pre_delete and post_delete implicitly point to a place in the
        document (where the two were split).  This moves that point (by
        popping items from one and pushing them onto the other).  It moves
        the point to try to find a place where unbalanced_start applies.
    
        As an example::
    
            >>> unbalanced_start = ['<div>']
            >>> doc = ['<p>', 'Text', '</p>', '<div>', 'More Text', '</div>']
            >>> pre, post = doc[:3], doc[3:]
            >>> pre, post
            (['<p>', 'Text', '</p>'], ['<div>', 'More Text', '</div>'])
            >>> locate_unbalanced_start(unbalanced_start, pre, post)
            >>> pre, post
            (['<p>', 'Text', '</p>', '<div>'], ['More Text', '</div>'])
    
        As you can see, we moved the point so that the dangling <div> that
        we found will be effectively replaced by the div in the original
        document.  If this doesn't work out, we just throw away
        unbalanced_start without doing anything.
    """
    pass

def markup_serialize_tokens(*args, **kwargs): # real signature unknown
    """
    Serialize the list of tokens into a list of text chunks, calling
        markup_func around text to add annotations.
    """
    pass

def merge_delete(*args, **kwargs): # real signature unknown
    """
    Adds the text chunks in del_chunks to the document doc (another
        list of text chunks) with marker to show it is a delete.
        cleanup_delete later resolves these markers into <del> tags.
    """
    pass

def merge_insert(*args, **kwargs): # real signature unknown
    """
    doc is the already-handled document (as a list of text chunks);
        here we add <ins>ins_chunks</ins> to the end of that.
    """
    pass

def parse_html(*args, **kwargs): # real signature unknown
    """
    Parses an HTML fragment, returning an lxml element.  Note that the HTML will be
        wrapped in a <div> tag that was not in the original document.
    
        If cleanup is true, make sure there's no <head> or <body>, and get
        rid of any <ins> and <del> tags.
    """
    pass

def serialize_html_fragment(*args, **kwargs): # real signature unknown
    """
    Serialize a single lxml element as HTML.  The serialized form
        includes the elements tail.  
    
        If skip_outer is true, then don't serialize the outermost tag
    """
    pass

def split_delete(*args, **kwargs): # real signature unknown
    """
    Returns (stuff_before_DEL_START, stuff_inside_DEL_START_END,
        stuff_after_DEL_END).  Returns the first case found (there may be
        more DEL_STARTs in stuff_after_DEL_END).  Raises NoDeletes if
        there's no DEL_START found.
    """
    pass

def split_trailing_whitespace(*args, **kwargs): # real signature unknown
    """
    This function takes a word, such as 'test
    
    ' and returns ('test','
    
    ')
    """
    pass

def split_unbalanced(*args, **kwargs): # real signature unknown
    """
    Return (unbalanced_start, balanced, unbalanced_end), where each is
        a list of text and tag chunks.
    
        unbalanced_start is a list of all the tags that are opened, but
        not closed in this span.  Similarly, unbalanced_end is a list of
        tags that are closed but were not opened.  Extracting these might
        mean some reordering of the chunks.
    """
    pass

def split_words(*args, **kwargs): # real signature unknown
    """
    Splits some text into words. Includes trailing whitespace
        on each word when appropriate.
    """
    pass

def start_tag(*args, **kwargs): # real signature unknown
    """ The text representation of the start tag for a tag. """
    pass

def tokenize(*args, **kwargs): # real signature unknown
    """
    Parse the given HTML and returns token objects (words with attached tags).
    
        This parses only the content of a page; anything in the head is
        ignored, and the <head> and <body> elements are themselves
        optional.  The content is then parsed by lxml, which ensures the
        validity of the resulting parsed document (though lxml may make
        incorrect guesses when the markup is particular bad).
    
        <ins> and <del> tags are also eliminated from the document, as
        that gets confusing.
    
        If include_hrefs is true, then the href attribute of <a> tags is
        included as a special kind of diffable token.
    """
    pass

def tokenize_annotated(*args, **kwargs): # real signature unknown
    """ Tokenize a document and add an annotation attribute to each token """
    pass

def _contains_block_level_tag(*args, **kwargs): # real signature unknown
    """ True if the element contains any block-level elements, like <p>, <td>, etc. """
    pass

def _fixup_ins_del_tags(*args, **kwargs): # real signature unknown
    """ fixup_ins_del_tags that works on an lxml document in-place """
    pass

def _merge_element_contents(*args, **kwargs): # real signature unknown
    """
    Removes an element, but merges its contents into its place, e.g.,
        given <p>Hi <i>there!</i></p>, if you remove the <i> element you get
        <p>Hi there!</p>
    """
    pass

def _move_el_inside_block(*args, **kwargs): # real signature unknown
    """
    helper for _fixup_ins_del_tags; actually takes the <ins> etc tags
        and moves them inside any block-level tags.
    """
    pass

# classes

class _unicode(object):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    """
    def capitalize(self): # real signature unknown; restored from __doc__
        """
        S.capitalize() -> str
        
        Return a capitalized version of S, i.e. make the first character
        have upper case and the rest lower case.
        """
        return ""

    def casefold(self): # real signature unknown; restored from __doc__
        """
        S.casefold() -> str
        
        Return a version of S suitable for caseless comparisons.
        """
        return ""

    def center(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.center(width[, fillchar]) -> str
        
        Return S centered in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return ""

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

    def encode(self, encoding='utf-8', errors='strict'): # real signature unknown; restored from __doc__
        """
        S.encode(encoding='utf-8', errors='strict') -> bytes
        
        Encode S using the codec registered for encoding. Default encoding
        is 'utf-8'. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
        'xmlcharrefreplace' as well as any other name registered with
        codecs.register_error that can handle UnicodeEncodeErrors.
        """
        return b""

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, tabsize=8): # real signature unknown; restored from __doc__
        """
        S.expandtabs(tabsize=8) -> str
        
        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return ""

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> str
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def format_map(self, mapping): # real signature unknown; restored from __doc__
        """
        S.format_map(mapping) -> str
        
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found, 
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def isalnum(self): # real signature unknown; restored from __doc__
        """
        S.isalnum() -> bool
        
        Return True if all characters in S are alphanumeric
        and there is at least one character in S, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        S.isalpha() -> bool
        
        Return True if all characters in S are alphabetic
        and there is at least one character in S, False otherwise.
        """
        return False

    def isdecimal(self): # real signature unknown; restored from __doc__
        """
        S.isdecimal() -> bool
        
        Return True if there are only decimal characters in S,
        False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        S.isdigit() -> bool
        
        Return True if all characters in S are digits
        and there is at least one character in S, False otherwise.
        """
        return False

    def isidentifier(self): # real signature unknown; restored from __doc__
        """
        S.isidentifier() -> bool
        
        Return True if S is a valid identifier according
        to the language definition.
        
        Use keyword.iskeyword() to test for reserved identifiers
        such as "def" and "class".
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        S.islower() -> bool
        
        Return True if all cased characters in S are lowercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def isnumeric(self): # real signature unknown; restored from __doc__
        """
        S.isnumeric() -> bool
        
        Return True if there are only numeric characters in S,
        False otherwise.
        """
        return False

    def isprintable(self): # real signature unknown; restored from __doc__
        """
        S.isprintable() -> bool
        
        Return True if all characters in S are considered
        printable in repr() or S is empty, False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        S.isspace() -> bool
        
        Return True if all characters in S are whitespace
        and there is at least one character in S, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        S.istitle() -> bool
        
        Return True if S is a titlecased string and there is at least one
        character in S, i.e. upper- and titlecase characters may only
        follow uncased characters and lowercase characters only cased ones.
        Return False otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        S.isupper() -> bool
        
        Return True if all cased characters in S are uppercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def join(self, iterable): # real signature unknown; restored from __doc__
        """
        S.join(iterable) -> str
        
        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.
        """
        return ""

    def ljust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.ljust(width[, fillchar]) -> str
        
        Return S left-justified in a Unicode string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""

    def lower(self): # real signature unknown; restored from __doc__
        """
        S.lower() -> str
        
        Return a copy of the string S converted to lowercase.
        """
        return ""

    def lstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.lstrip([chars]) -> str
        
        Return a copy of the string S with leading whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table usable for str.translate().
        
        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        pass

    def partition(self, sep): # real signature unknown; restored from __doc__
        """
        S.partition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, and return the part before it,
        the separator itself, and the part after it.  If the separator is not
        found, return S and two empty strings.
        """
        pass

    def replace(self, old, new, count=None): # real signature unknown; restored from __doc__
        """
        S.replace(old, new[, count]) -> str
        
        Return a copy of S with all occurrences of substring
        old replaced by new.  If the optional argument count is
        given, only the first count occurrences are replaced.
        """
        return ""

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def rjust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.rjust(width[, fillchar]) -> str
        
        Return S right-justified in a string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""

    def rpartition(self, sep): # real signature unknown; restored from __doc__
        """
        S.rpartition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, starting at the end of S, and return
        the part before it, the separator itself, and the part after it.  If the
        separator is not found, return two empty strings and S.
        """
        pass

    def rsplit(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
        """
        S.rsplit(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string, starting at the end of the string and
        working to the front.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified, any whitespace string
        is a separator.
        """
        return []

    def rstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.rstrip([chars]) -> str
        
        Return a copy of the string S with trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def split(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
        """
        S.split(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are
        removed from the result.
        """
        return []

    def splitlines(self, keepends=None): # real signature unknown; restored from __doc__
        """
        S.splitlines([keepends]) -> list of strings
        
        Return a list of the lines in S, breaking at line boundaries.
        Line breaks are not included in the resulting list unless keepends
        is given and true.
        """
        return []

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.strip([chars]) -> str
        
        Return a copy of the string S with leading and trailing
        whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        S.swapcase() -> str
        
        Return a copy of S with uppercase characters converted to lowercase
        and vice versa.
        """
        return ""

    def title(self): # real signature unknown; restored from __doc__
        """
        S.title() -> str
        
        Return a titlecased version of S, i.e. words start with title case
        characters, all remaining cased characters have lower case.
        """
        return ""

    def translate(self, table): # real signature unknown; restored from __doc__
        """
        S.translate(table) -> str
        
        Return a copy of the string S in which each character has been mapped
        through the given translation table. The table must implement
        lookup/indexing via __getitem__, for instance a dictionary or list,
        mapping Unicode ordinals to Unicode ordinals, strings, or None. If
        this operation raises LookupError, the character is left untouched.
        Characters mapped to None are deleted.
        """
        return ""

    def upper(self): # real signature unknown; restored from __doc__
        """
        S.upper() -> str
        
        Return a copy of S converted to uppercase.
        """
        return ""

    def zfill(self, width): # real signature unknown; restored from __doc__
        """
        S.zfill(width) -> str
        
        Pad a numeric string S with zeros on the left, to fill a field
        of the specified width. The string S is never truncated.
        """
        return ""

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, format_spec): # real signature unknown; restored from __doc__
        """
        S.__format__(format_spec) -> str
        
        Return a formatted version of S as described by format_spec.
        """
        return ""

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value.n """
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

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


basestring = _unicode


class DEL_END(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'lxml.html.diff', '__dict__': <attribute '__dict__' of 'DEL_END' objects>, '__weakref__': <attribute '__weakref__' of 'DEL_END' objects>, '__doc__': None})"


class DEL_START(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'lxml.html.diff', '__dict__': <attribute '__dict__' of 'DEL_START' objects>, '__weakref__': <attribute '__weakref__' of 'DEL_START' objects>, '__doc__': None})"


class token(str):
    """
    Represents a diffable token, generally a word that is displayed to
        the user.  Opening tags are attached to this token when they are
        adjacent (pre_tags) and closing tags that follow the word
        (post_tags).  Some exceptions occur when there are empty tags
        adjacent to a word, so there may be close tags in pre_tags, or
        open tags in post_tags.
    
        We also keep track of whether the word was originally followed by
        whitespace, even though we do not want to treat the word as
        equivalent to a similar word that does not have a trailing
        space.
    """
    def html(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    hide_when_equal = False
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'lxml.html.diff', '__doc__': ' Represents a diffable token, generally a word that is displayed to\\n    the user.  Opening tags are attached to this token when they are\\n    adjacent (pre_tags) and closing tags that follow the word\\n    (post_tags).  Some exceptions occur when there are empty tags\\n    adjacent to a word, so there may be close tags in pre_tags, or\\n    open tags in post_tags.\\n\\n    We also keep track of whether the word was originally followed by\\n    whitespace, even though we do not want to treat the word as\\n    equivalent to a similar word that does not have a trailing\\n    space.', 'hide_when_equal': False, '__new__': <cyfunction token.__new__ at 0x7fd10df0f6c0>, '__repr__': <cyfunction token.__repr__ at 0x7fd10df0f778>, 'html': <cyfunction token.html at 0x7fd10df0f830>, '__dict__': <attribute '__dict__' of 'token' objects>, '__weakref__': <attribute '__weakref__' of 'token' objects>})"


class href_token(token):
    """
    Represents the href in an anchor tag.  Unlike other words, we only
        show the href when it changes.
    """
    def html(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    hide_when_equal = True


class InsensitiveSequenceMatcher(__difflib.SequenceMatcher):
    """
    Acts like SequenceMatcher, but tries not to find very small equal
        blocks amidst large spans of changes
    """
    def get_matching_blocks(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, isjunk=None, a=None, b=None, autojunk=True): # reliably restored by inspect
        """
        Construct a SequenceMatcher.
        
                Optional arg isjunk is None (the default), or a one-argument
                function that takes a sequence element and returns true iff the
                element is junk.  None is equivalent to passing "lambda x: 0", i.e.
                no elements are considered to be junk.  For example, pass
                    lambda x: x in " \t"
                if you're comparing lines as sequences of characters, and don't
                want to synch up on blanks or hard tabs.
        
                Optional arg a is the first of two sequences to be compared.  By
                default, an empty string.  The elements of a must be hashable.  See
                also .set_seqs() and .set_seq1().
        
                Optional arg b is the second of two sequences to be compared.  By
                default, an empty string.  The elements of b must be hashable. See
                also .set_seqs() and .set_seq2().
        
                Optional arg autojunk should be set to False to disable the
                "automatic junk heuristic" that treats popular elements as junk
                (see module documentation for more information).
        """
        pass

    threshold = 2


class NoDeletes(Exception):
    """
    Raised when the document no longer contains any pending deletes
        (DEL_START/DEL_END)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class tag_token(token):
    """
    Represents a token that is actually a tag.  Currently this is just
        the <img> tag, which takes up visible space just like a word but
        is only represented in a document by a tag.
    """
    def html(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

block_level_container_tags = (
    'dd',
    'dt',
    'frameset',
    'li',
    'tbody',
    'td',
    'tfoot',
    'th',
    'thead',
    'tr',
)

block_level_tags = (
    'address',
    'blockquote',
    'center',
    'dir',
    'div',
    'dl',
    'fieldset',
    'form',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'hr',
    'isindex',
    'menu',
    'noframes',
    'noscript',
    'ol',
    'p',
    'pre',
    'table',
    'ul',
)

empty_tags = (
    'param',
    'img',
    'area',
    'br',
    'basefont',
    'input',
    'base',
    'meta',
    'link',
    'col',
)

end_whitespace_re = None # (!) real value is "re.compile('[ \\\\t\\\\n\\\\r]$')"

split_words_re = None # (!) real value is "re.compile('\\\\S+(?:\\\\s+|$)')"

start_whitespace_re = None # (!) real value is "re.compile('^[ \\\\t\\\\n\\\\r]')"

_body_re = None # (!) real value is "re.compile('<body.*?>', re.IGNORECASE|re.DOTALL)"

_end_body_re = None # (!) real value is "re.compile('</body.*?>', re.IGNORECASE|re.DOTALL)"

_ins_del_re = None # (!) real value is "re.compile('</?(ins|del).*?>', re.IGNORECASE|re.DOTALL)"

__all__ = [
    'html_annotate',
    'htmldiff',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd10de5d1d0>'

__spec__ = None # (!) real value is "ModuleSpec(name='lxml.html.diff', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd10de5d1d0>, origin='/home/sarthak/Programming/CricketPlayerDataScrapper/venv/lib/python3.6/site-packages/lxml/html/diff.cpython-36m-x86_64-linux-gnu.so')"

__test__ = {
    'html_annotate (line 35)': '\n    doclist should be ordered from oldest to newest, like::\n\n        >>> version1 = \'Hello World\'\n        >>> version2 = \'Goodbye World\'\n        >>> print(html_annotate([(version1, \'version 1\'),\n        ...                      (version2, \'version 2\')]))\n        <span title="version 2">Goodbye</span> <span title="version 1">World</span>\n\n    The documents must be *fragments* (str/UTF8 or unicode), not\n    complete documents\n\n    The markup argument is a function to markup the spans of words.\n    This function is called like markup(\'Hello\', \'version 2\'), and\n    returns HTML.  The first argument is text and never includes any\n    markup.  The default uses a span with a title:\n\n        >>> print(default_markup(\'Some Text\', \'by Joe\'))\n        <span title="by Joe">Some Text</span>\n    ',
    'locate_unbalanced_start (line 365)': " pre_delete and post_delete implicitly point to a place in the\n    document (where the two were split).  This moves that point (by\n    popping items from one and pushing them onto the other).  It moves\n    the point to try to find a place where unbalanced_start applies.\n\n    As an example::\n\n        >>> unbalanced_start = ['<div>']\n        >>> doc = ['<p>', 'Text', '</p>', '<div>', 'More Text', '</div>']\n        >>> pre, post = doc[:3], doc[3:]\n        >>> pre, post\n        (['<p>', 'Text', '</p>'], ['<div>', 'More Text', '</div>'])\n        >>> locate_unbalanced_start(unbalanced_start, pre, post)\n        >>> pre, post\n        (['<p>', 'Text', '</p>', '<div>'], ['More Text', '</div>'])\n\n    As you can see, we moved the point so that the dangling <div> that\n    we found will be effectively replaced by the div in the original\n    document.  If this doesn't work out, we just throw away\n    unbalanced_start without doing anything.\n    ",
}

