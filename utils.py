import json

import os


def load_json(filepath='data.json') -> dict:
    """Load json file from disk"""
    with open(filepath, 'r') as f:
        return json.load(f)


def save_json(filepath: str, data: dict) -> None:
    """Save json file to disk"""
    with open(filepath, 'w') as f:
        return json.dump(data, f, indent=2)
