from idx_generator import IdxGenerator
from input_stream import FileInputStream

if __name__ == '__main__':
    fis = FileInputStream('D:/test/tmp.rec')
    idxg = IdxGenerator(fis)
    idxg.generate_idx_file( 'D:/test/1.idx')
