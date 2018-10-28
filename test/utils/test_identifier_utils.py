from unittest import TestCase
from utils import IdentifierUtils, TypeConvertor


class TestIdentifierUtils(TestCase):
    def test_get_code(self):
        num = 3 << 29;
        t_bytes = TypeConvertor.int2bytes(num)
        self.assertEqual(3, IdentifierUtils.get_code(t_bytes))

    def test_get_length(self):
        t_bytes = bytes.fromhex('07 00 00 00')
        self.assertEqual(7, IdentifierUtils.get_length(t_bytes))
