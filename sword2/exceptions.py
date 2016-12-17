#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Provides various Exception classes to match HTTP error code responses.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library
standard_library.install_aliases()
from builtins import *
class HTTPResponseError(Exception):
    """Generic exception for http codes greater than 399 and less than 599 """
    def __init__(self, response=None, content=None):
        self.response = response
        self.content = content
        
class ServerError(HTTPResponseError):
    """ for http error codes 500 and up """
    pass

class NotAuthorised(HTTPResponseError):
    pass

class Forbidden(HTTPResponseError):
    pass

class RequestTimeOut(HTTPResponseError):
    pass

class NotFound(HTTPResponseError):
    pass

class PackagingFormatNotAvailable(HTTPResponseError):
    pass

class NotAcceptable(HTTPResponseError):
    pass
