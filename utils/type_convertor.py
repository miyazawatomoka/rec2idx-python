class TypeConvertor:
    @staticmethod
    def btyes2int(t_bytes):
        return int.from_bytes(t_bytes, byteorder='little', signed=False)

    @staticmethod
    def int2bytes(num):
        return num.to_bytes(4, byteorder='little', signed=False)



