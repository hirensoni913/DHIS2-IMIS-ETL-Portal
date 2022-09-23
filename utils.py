import json
import os
from functools import lru_cache, wraps
from datetime import datetime, timedelta

from dotenv import load_dotenv


def timed_lru_cache(seconds: int, maxsize: int = 128):
    """Cache decorator for caching
    - seconds: how long until it expires
    - maxsize: how many entries it can hold
    """

    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache


@timed_lru_cache(seconds=10)
def load_data(filepath: str) -> dict:
    """Load json file from disk"""
    with open(filepath, 'r') as f:
        return json.load(f)


def save_json(filepath: str, data: dict) -> None:
    """Save json file to disk"""
    with open(filepath, 'w') as f:
        return json.dump(data, f, indent=2)


def get_dhis2_credentials():
    """Load DHIS2 credentials from environment"""
    load_dotenv()

    username = os.getenv('DHIS2USERNAME')
    password = os.getenv('DHIS2PASSWORD')
    base_url = os.getenv('DHIS2BASEURL')

    if not username:
        raise ValueError("Environment variable not found: 'DHIS2USERNAME'")
    if not password:
        raise ValueError("Environment variable not found: 'DHIS2PASSWORD'")
    if not base_url:
        raise ValueError("DHIS2BASEURL environment variable not set")
    if not base_url.startswith('http'):
        raise ValueError("DHIS2BASEURL invalid - http:// or https:// not found")
    if base_url.endswith("/"):
        raise ValueError("DHIS2BASEURL invalid - no trailing slash")
    return base_url, username, password
