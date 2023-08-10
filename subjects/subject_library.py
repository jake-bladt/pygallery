import file_operations as fileops
import s3_operations as s3ops
import subject_utils as utils

class SubjectLibrary:
    def __init__(self, subject):
        self.subject = subject
        self.batch_started = False
        self.is_dirty = False

    def start_batch(self):
        self.manifest = s3ops.get_subject_hashes(self.subject)
        self.subject_local_path = utils.get_subject_directory_path(self.subject)
        self.batch_results = []
        self.batch_started = True

    def end_batch(self):
        self.batch_started = False
        return self.batch_results

    def write_if_needed(self, filename):
        if(not self.batch_started):
            raise 'Illegal batch operation outside of batch.'

        hash = fileops.get_file_hash(filename)
        needs_write = filename not in self.manifest or self.manifest[filename] != hash
        ret = ''

        if(needs_write):
            full_path = f'{self.subject_local_path}{filename}'
            write_result = s3ops.write_file_to_s3(self.subject, full_path)
            if(write_result):
                self.manifest[filename] = hash
                self.is_dirty = True
                ret = f'Wrote {filename} to s3.'
            else:
                ret = f'Failed to write {filename} to s3.'
        else:
            ret = f'Skipped {filename}.'

        self.batch_results.push(ret)    
        return ret
    
    def write_manifest():
        pass
    