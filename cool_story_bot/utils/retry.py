import time
from functools import wraps


def retry(exception_to_check, tries=5, delay=3):
    """
    Retry calling the decorated function.

    :param exception_to_check: the exception to check for
    :param tries: maximum amount of times to try
    :param delay: initial delay between retries
    """
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, *kwargs)
                except exception_to_check as e:
                    print("{}: {}, retrying in {} seconds...".format(exception_to_check.__name__, str(e), mdelay))
                    time.sleep(mdelay)
                    mtries -= 1
                    if mtries <= 1:
                        print("{} failed too many times ({}).".format(f.__name__, tries))
            return f(*args, **kwargs)
        return f_retry
    return deco_retry
