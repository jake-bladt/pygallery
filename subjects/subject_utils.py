import os

subject_root = os.getenv('GALLERY_SUBJECT_ROOT')

def get_subject_directory_path(subject):
    return subject_root + subject + "\\"

def get_s3_file_target_path(subject, file_path):
    file_name = file_path.split("\\")[-1]
    return f'gallery/{subject}/{file_name}'

def get_s3_subject_manifest_path(subject):
    return f'gallery/{subject}/.manifest'
