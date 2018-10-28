from .type_convertor import TypeConvertor


class IdentifierUtils:
    MAGIC = 0xced7230a
    WITH_OUT_MAGIC_CODE = 0
    FIRST_MAGIC_CODE = 1
    OTHERS_MAGIC_CODE = 2
    WIHT_MAGIC_CODE = 3
    FLAG_MOVE_BIT = 29
    MAGIC_BYTES = TypeConvertor.int2bytes(MAGIC)
    INT_BYTES = 4

    @staticmethod
    def get_code(identifier_bytes):
        return identifier_bytes[IdentifierUtils.INT_BYTES - 1] >> 5

    @staticmethod
    def get_length(identifier_bytes):
        identifier_num = TypeConvertor.btyes2int(identifier_bytes)
        return (identifier_num << IdentifierUtils.INT_BYTES) >> IdentifierUtils.INT_BYTES

    @staticmethod
    def is_magic(t_bytes):
        for i in range(IdentifierUtils.INT_BYTES):
            if IdentifierUtils.MAGIC_BYTES[i] != t_bytes[i]:
                return False
        return True




