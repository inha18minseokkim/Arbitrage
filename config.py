import json
from pathlib import Path
from typing import Optional
BASE_DIR = Path(__file__).resolve().parent
def get_secret(key: str):
    with open(str(BASE_DIR / 'secrets.json')) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[key]
    except KeyError:
        return ""
if __name__ == '__main__':
    print(BASE_DIR)