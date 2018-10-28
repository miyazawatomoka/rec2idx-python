from unittest import TestCase
from utils import IdentifierUtils, TypeConvertor


class TestTypeConvertor(TestCase):
    def test_btyes2int(self):
        t_bytes = bytes.fromhex('0A 23 D7 CE')
        self.assertEqual(IdentifierUtils.MAGIC, TypeConvertor.btyes2int(t_bytes))

    def test_int2bytes(self):
        t_bytes = bytes.fromhex('0A 23 D7 CE')
        # pdb.set_trace()
        self.assertEqual(t_bytes, TypeConvertor.int2bytes(IdentifierUtils.MAGIC))

