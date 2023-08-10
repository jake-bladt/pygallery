subject_root = "H:\\shared_root\\jake\\bulk\\regal\\bins\\cast\\subjects\\"

def get_subject_directory_path(subject):
    return subject_root + subject + "\\"

def get_s3_target_path(subject, file_path):
    file_name = file_path.split("\\")[-1]
    return f'gallery/{subject}/{file_name}'
