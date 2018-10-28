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
    def seek_from_current(self, length):
        """
        seek the file pointer from current to current + length,
        implements it need pay attention at 4 bit align
        if filesystem don't support seek, implements it with a pass

        """
        pass
