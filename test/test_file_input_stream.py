from unittest import TestCase
from input_stream import FileInputStream


class TestFileInputStream(TestCase):
    def test_klass(self):
        FileInputStream('./resources/tmp.rec')

    def test_has_next_four_bytes(self):
        fis = FileInputStream('./resources/tmp.rec')
        assert fis.has_next_four_bytes()

    def test_get_next_four_bytes(self):
        fis = FileInputStream('./resources/tmp.rec')
        idx, bytes = fis.get_next_four_bytes()
        self.assertEqual(bytes[3], 0xCE)
        self.assertEqual(0, idx)
        idx, bytes = fis.get_next_four_bytes()
        self.assertEqual(bytes[3], 0x00)
        self.assertEqual(4, idx)
