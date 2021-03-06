from utils import IdentifierUtils


class IdxGenerator:
    def __init__(self, input_stream):
        self.input_stream = input_stream

    def get_idx_list(self):
        idx_list = []
        last_magic_idx = 0
        is_prev_magic = False
        while self.input_stream.has_next_four_bytes():
            cur_idx, cur_bytes = self.input_stream.get_next_four_bytes()
            if IdentifierUtils.is_magic(cur_bytes):
                last_magic_idx = cur_idx
                is_prev_magic = True
            else:
                if is_prev_magic:
                    t_code = IdentifierUtils.get_code(cur_bytes)
                    if t_code == IdentifierUtils.FIRST_MAGIC_CODE or t_code == IdentifierUtils.WITH_OUT_MAGIC_CODE:
                        idx_list.append(last_magic_idx)
                    length = IdentifierUtils.get_length(cur_bytes)
                    offset = ((length + 3) >> 2) << 2
                    self.input_stream.seek_from_current(offset)
                is_prev_magic = False
        return idx_list

    def generate_idx_file(self, idx_target_path):
        with open(idx_target_path, mode='w') as idx_file:
            idx_list = self.get_idx_list()
            for index, idx in enumerate(idx_list):
                idx_file.write("%d\t%d\n" % (index, idx))



