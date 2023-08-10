import sys

import file_operations as fileops
import subject_utils as utils
import s3_operations as s3ops

def copy_subject_directory(subject):
    full_path = utils.get_subject_directory_path(subject)
    print(f'Uploading from {full_path}...')
    existing_hashes = s3ops.get_subject_hashes(subject)
    print(existing_hashes)

    all_jpgs = fileops.get_files_with_extension(full_path, 'jpg')
    for j in all_jpgs:
        jpg_path = f'{full_path}{j}'
        hash = fileops.get_file_hash(jpg_path)
        write_success = s3ops.write_file_to_s3(subject, jpg_path)
        action = "Copied file" if write_success else "Failed to copy file"
        print(f'{action} {j} with hash {hash} to s3')

if __name__ == "__main__":
    subject = sys.argv[1]
    copy_subject_directory(subject)
