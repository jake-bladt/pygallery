import hashlib
import os

def get_file_hash(filename):
    with open(filename, "rb") as f:
        bytes = f.read()
        hash = hashlib.md5(bytes).hexdigest()
        return hash

def get_files_with_extension(path, ext):
    all_files = os.listdir(path)
    ending = ext if ext.startswith('.') else f'.{ext}'
    return [f for f in all_files if f.endswith(ending)]
