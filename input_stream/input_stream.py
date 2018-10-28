from abc import ABCMeta, abstractmethod


class InputStream (metaclass=ABCMeta):
    @abstractmethod
    def has_next_four_bytes(self):
        """
        return:
            True or False
        """
        pass

    @abstractmethod
    def get_next_four_bytes(self):
        """
        returns:
            offset: Return offset at begin of the four bytes
            t_bytes: Next four bytes
        """
        pass

    @abstractmethod
    def seek(self, offset):
        """
        seek the file pointer from current to current + offset
        """
        pass
