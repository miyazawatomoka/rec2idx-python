from .input_stream import InputStream
import os


class FileInputStream(InputStream):
    def __init__(self, rec_path):
        self.rec_path = rec_path
        try:
            self.rec_file = open(rec_path, 'rb')
            self.file_bytes_len = os.path.getsize(rec_path)
        except IOError as err:
            self.rec_file.close()
            raise err

    def get_next_four_bytes(self):
        try:
            t_bytes = self.rec_file.read(4)
        except IOError as err:
            self.rec_file.close()
            raise err
        return self.rec_file.tell() - 4, t_bytes

    def has_next_four_bytes(self):
        if self.file_bytes_len - self.rec_file.tell() >= 4:
            return True
        else:
            return False

    def seek_from_current(self, offset):
        self.rec_file.seek(self.rec_file.tell() + offset)
