from idx_generator import IdxGenerator
from input_stream import FileInputStream

if __name__ == '__main__':
    fis = FileInputStream('D:/test/tmp.rec')
    idxg = IdxGenerator(fis, 'D:/test/1.idx')
    idxg.generate_idx_file()
