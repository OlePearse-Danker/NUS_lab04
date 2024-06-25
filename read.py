from struct import unpack

def binary(fname):
    with open(fname, 'rb') as f:
        n = unpack('i', f.read(4))[0]
        U = unpack('d' * n, f.read(8 * n))
        I = unpack('d' * n, f.read(8 * n))
    return I, U