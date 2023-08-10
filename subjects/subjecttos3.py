import boto3
import hashlib
import os
import sys

from botocore.exceptions import ClientError

import subject_utils as utils

subject_root = "H:\\shared_root\\jake\\bulk\\regal\\bins\\cast\\subjects\\"
s3_bucket_name = 'jakecodes-gallery-dev1'
s3_client = boto3.client('s3')

def get_file_hash(filename):
    with open(filename, "rb") as f:
        bytes = f.read()
        hash = hashlib.md5(bytes).hexdigest()
        return hash

def write_file_to_s3(subject, source_path):
    target_path = utils.get_s3_target_path(subject, source_path)
    try:
        response = s3_client.upload_file(source_path, s3_bucket_name, target_path)
    except ClientError as e:
        print(e)
        return False
    return True

def get_jpgs(path):
    all_files = os.listdir(path)
    return [f for f in all_files if f.endswith(".jpg")]

def copy_subject_directory(subject):
    full_path = utils.get_subject_directory_path(subject)
    print(f'Uploading from {full_path}...')
    all_jpgs = get_jpgs(full_path)
    for j in all_jpgs:
        jpg_path = f'{full_path}{j}'
        hash = get_file_hash(jpg_path)
        write_success = write_file_to_s3(subject, jpg_path)
        action = "Copied file" if write_success else "Failed to copy file"
        print(f'{action} {j} with hash {hash} to s3')

if __name__ == "__main__":
    subject = sys.argv[1]
    copy_subject_directory(subject)
