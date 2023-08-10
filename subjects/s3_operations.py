import boto3
from botocore.exceptions import ClientError

import subject_utils as utils

s3_bucket_name = 'jakecodes-gallery-dev1'
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

def write_file_to_s3(subject, source_path):
    target_path = utils.get_s3_file_target_path(subject, source_path)
    try:
        response = s3_client.upload_file(source_path, s3_bucket_name, target_path)
    except ClientError as e:
        print(e)
        return False
    return True

def object_exists(bucket, path):
    bucket = s3_resource.Bucket(bucket)
    objs = list(bucket.objects.filter(Prefix=path))
    keys = set(o.key for o in objs)
    return path in keys

def get_subject_hashes(subject):
    manifest_path = utils.get_s3_subject_manifest_path(subject)
    ret = {}
    if(object_exists(s3_bucket_name, manifest_path)):
        read_response = s3_client.get_object(
            Bucket=s3_bucket_name,
            Key=manifest_path
        )

        body = read_response.get('Body')
        manifest_string = body.read().decode()
        manifest_entries = manifest_string.splitlines()
        for entry in manifest_entries:
            parts = entry.split[':']
            ret[parts[0]] = parts[1]

    return ret
