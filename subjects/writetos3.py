import sys

import file_operations as fileops
import subject_utils as utils

from subject_library import SubjectLibrary

def copy_subject_directory(subject):
    library = SubjectLibrary(subject)
    library.start_batch()

    local_source_path = utils.get_subject_directory_path(subject)
    all_jpgs = fileops.get_files_with_extension(local_source_path, 'jpg')
    for j in all_jpgs:
        library.write_if_needed(j)

    batch_results = library.end_batch()
    for r in batch_results:
        print(r)

if __name__ == "__main__":
    subject = sys.argv[1]
    copy_subject_directory(subject)
