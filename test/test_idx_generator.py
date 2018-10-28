from unittest import TestCase
from input_stream import FileInputStream
from idx_generator import IdxGenerator


class TestIdxGenerator(TestCase):
    def test_get_idx_list(self):
        fis = FileInputStream('./resources/tmp.rec')
        idxg = IdxGenerator(fis)
        idx_list = idxg.get_idx_list()
        true_idx_list = [0, 8, 24, 48, 80, 116, 160, 212, 272, 336, 408, 488, 576, 668, 768, 876]
        self.assertListEqual(idx_list, true_idx_list)

