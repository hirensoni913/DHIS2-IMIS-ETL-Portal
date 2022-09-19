import json
import os

from dotenv import load_dotenv


def load_json(filepath='data.json') -> dict:
    """Load json file from disk"""
    with open(filepath, 'r') as f:
        return json.load(f)


def save_json(filepath: str, data: dict) -> None:
    """Save json file to disk"""
    with open(filepath, 'w') as f:
        return json.dump(data, f, indent=2)


def get_dhis2_base_url():
    load_dotenv()
    base_url = os.getenv('DHIS2BASEURL')
    if not base_url:
        raise ValueError("DHIS2BASEURL environment variable not set")
    if not base_url.startswith('http'):
        raise ValueError("DHIS2BASEURL invalid - http:// or https:// not found")
    if base_url.endswith("/"):
        raise ValueError("DHIS2BASEURL invalid - no trailing slash")
    return base_url
