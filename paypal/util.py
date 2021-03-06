# -*- coding: utf-8 -*-

import logging

#: Main logger utilized across the entire library
logger = logging.getLogger('paypal.core')
#: Restricted logger which is intended to only log API
#: requests and responses along with potential errors
#: associated with them.
api_logger = logging.getLogger('paypal.api')
#: Restricted logger which is intended to only log
#: Instant Payment Notifications (IPN) from PayPal along
#: with the verification for each notification.
ipn_logger = logging.getLogger('paypal.ipn')


class LoggingNullHandler(logging.Handler):
    """Logging handler which emits nothing."""
    def emit(self, record):
        pass


logger.addHandler(LoggingNullHandler())
api_logger.addHandler(LoggingNullHandler())
ipn_logger.addHandler(LoggingNullHandler())


def generate_utc_string(utc_datetime):
    return utc_datetime.strftime('%Y-%m-%dT%H-%M-%SZ')


def ensure_unicode(obj):
    """Recursively encode the given ``obj`` to unicode.

    Credit should go out to Ben Darnell for this one since the code
    is a modification of the solution in tornado.

    :param obj: The object to walk through and encode contained values
    """
    if isinstance(obj, (unicode, type(None))):
        return obj

    if isinstance(obj, dict):
        items = obj.iteritems()
        return dict((ensure_unicode(k), ensure_unicode(v)) for k, v in items)
    elif isinstance(obj, (list, tuple)):
        return type(obj)(ensure_unicode(i) for i in obj)
    elif isinstance(obj, bytes):
        return obj.decode('utf-8')
    return obj
