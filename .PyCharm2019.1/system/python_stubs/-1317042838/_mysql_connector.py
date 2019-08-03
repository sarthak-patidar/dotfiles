# encoding: utf-8
# module _mysql_connector
# from /var/www/newsbytes/CPP/venv/lib/python3.6/site-packages/_mysql_connector.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
""" Python C Extension using MySQL Connector/C """
# no imports

# functions

def datetime_to_mysql(*args, **kwargs): # real signature unknown
    """ Convert a Python datetime.datetime to MySQL DATETIME """
    pass

def date_to_mysql(*args, **kwargs): # real signature unknown
    """ Convert a Python datetime.date to MySQL DATE """
    pass

def time_to_mysql(*args, **kwargs): # real signature unknown
    """ Convert a Python datetime.time to MySQL TIME """
    pass

# classes

class MySQL(object):
    """ MySQL objects """
    def affected_rows(self, *args, **kwargs): # real signature unknown
        """ Returns num of rows changed by the last statement """
        pass

    def autocommit(self, *args, **kwargs): # real signature unknown
        """ Set autocommit mode """
        pass

    def buffered(self, *args, **kwargs): # real signature unknown
        """ Set and get current setting of buffered """
        pass

    def change_user(self, *args, **kwargs): # real signature unknown
        """ Changes the user and causes db to become the default """
        pass

    def character_set_name(self, *args, **kwargs): # real signature unknown
        """ Returns the default character set name for the current connection """
        pass

    def close(self, *args, **kwargs): # real signature unknown
        """ Closes an open connection. """
        pass

    def commit(self, *args, **kwargs): # real signature unknown
        """ Commits the current transaction """
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        """ Connect with a MySQL server """
        pass

    def connected(self, *args, **kwargs): # real signature unknown
        """ Returns True when connected; False otherwise """
        pass

    def consume_result(self, *args, **kwargs): # real signature unknown
        """ Consumes the result by reading all rows """
        pass

    def convert_to_mysql(self, *args, **kwargs): # real signature unknown
        """ Convert Python objects to MySQL values """
        pass

    def escape_string(self, *args, **kwargs): # real signature unknown
        """ Create a legal SQL string that you can use in an SQL statement """
        pass

    def fetch_fields(self, *args, **kwargs): # real signature unknown
        """ Fetch information about fields in result set """
        pass

    def fetch_row(self, *args, **kwargs): # real signature unknown
        """ Fetch a row """
        pass

    def field_count(self, *args, **kwargs): # real signature unknown
        """ Returns number of columns for the most recent query """
        pass

    def free_result(self, *args, **kwargs): # real signature unknown
        """ Returns number of columns for the most recent query """
        pass

    def get_character_set_info(self, *args, **kwargs): # real signature unknown
        """ Provides information about the default client character set """
        pass

    def get_client_info(self, *args, **kwargs): # real signature unknown
        """ Returns a string that represents the client library version """
        pass

    def get_client_version(self, *args, **kwargs): # real signature unknown
        """ Returns a tuple that represents the client library version """
        pass

    def get_host_info(self, *args, **kwargs): # real signature unknown
        """ Returns a string describing the type of connection in use """
        pass

    def get_proto_info(self, *args, **kwargs): # real signature unknown
        """ Returns the protocol version used by current connection """
        pass

    def get_server_info(self, *args, **kwargs): # real signature unknown
        """ Returns a string that represents the server version number """
        pass

    def get_server_version(self, *args, **kwargs): # real signature unknown
        """ Returns the version number of the server as a tuple """
        pass

    def get_ssl_cipher(self, *args, **kwargs): # real signature unknown
        """ Returns the SSL cipher used for the given connection """
        pass

    def hex_string(self, *args, **kwargs): # real signature unknown
        """ Encode string in hexadecimal format """
        pass

    def insert_id(self, *args, **kwargs): # real signature unknown
        """ Returns the value generated for an AUTO_INCREMENT column """
        pass

    def more_results(self, *args, **kwargs): # real signature unknown
        """ Returns True if more results exists """
        pass

    def next_result(self, *args, **kwargs): # real signature unknown
        """ Reads next statement result and returns if more results are available """
        pass

    def num_fields(self, *args, **kwargs): # real signature unknown
        """ Returns number of fields in result set """
        pass

    def num_rows(self, *args, **kwargs): # real signature unknown
        """ Returns number of rows in result set """
        pass

    def ping(self, *args, **kwargs): # real signature unknown
        """ Checks whether the connection to the server is working """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """ Execute the SQL statement """
        pass

    def raw(self, *args, **kwargs): # real signature unknown
        """ Set and get current raw setting """
        pass

    def refresh(self, *args, **kwargs): # real signature unknown
        """ Flush tables, caches or reset replication server info """
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        """ Rolls back the current transaction """
        pass

    def select_db(self, *args, **kwargs): # real signature unknown
        """ Causes the database specified by db to become the default database """
        pass

    def set_character_set(self, *args, **kwargs): # real signature unknown
        """ Set the default character set for the current connection """
        pass

    def shutdown(self, *args, **kwargs): # real signature unknown
        """ Ask MySQL server to shut down """
        pass

    def stat(self, *args, **kwargs): # real signature unknown
        """ Returns server information like uptime, running threads, .. """
        pass

    def st_affected_rows(self, *args, **kwargs): # real signature unknown
        """ Returns affected rows """
        pass

    def st_client_flag(self, *args, **kwargs): # real signature unknown
        """ Returns client flags for current session """
        pass

    def st_field_count(self, *args, **kwargs): # real signature unknown
        """ Returns field count """
        pass

    def st_insert_id(self, *args, **kwargs): # real signature unknown
        """ Returns insert ID """
        pass

    def st_server_capabilities(self, *args, **kwargs): # real signature unknown
        """ Returns server capabilities """
        pass

    def st_server_status(self, *args, **kwargs): # real signature unknown
        """ Returns server status flag """
        pass

    def st_warning_count(self, *args, **kwargs): # real signature unknown
        """ Returns warning count """
        pass

    def thread_id(self, *args, **kwargs): # real signature unknown
        """ Returns the thread ID of the current connection """
        pass

    def use_unicode(self, *args, **kwargs): # real signature unknown
        """ Set and get current use_unicode setting """
        pass

    def warning_count(self, *args, **kwargs): # real signature unknown
        """ Returns the number of errors, warnings, and notes """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    have_result_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if current session has result set"""



class MySQLError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class MySQLInterfaceError(MySQLError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f442d080ac8>'

__spec__ = None # (!) real value is "ModuleSpec(name='_mysql_connector', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f442d080ac8>, origin='/var/www/newsbytes/CPP/venv/lib/python3.6/site-packages/_mysql_connector.cpython-36m-x86_64-linux-gnu.so')"

