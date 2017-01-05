import csv
import numpy as np

FILENAME = 'data/sms.txt'

def read_lines(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        return [ row[-1] for row in list(reader) ]

def index_(lines):
    vocab = list(set('\n'.join(lines)))
    ch2idx = { k:v for v,k in enumerate(vocab) }
    return vocab, ch2idx

def to_array(lines, seqlen, ch2idx):
    # combine into one string
    raw_data = '\n'.join(lines)
    num_chars = len(raw_data)
    # calc data_len
    data_len = num_chars//seqlen
    # create numpy arrays
    X = np.zeros([data_len, seqlen])
    Y = np.zeros([data_len, seqlen])
    # fill in
    for i in range(0, data_len):
        X[i] = np.array([ ch2idx[ch] for ch in raw_data[i*seqlen:(i+1)*seqlen] ])
        Y[i] = np.array([ ch2idx[ch] for ch in raw_data[(i*seqlen) + 1 : ((i+1)*seqlen) + 1] ])
    # return ndarrays
    return X, Y

def process_data(seqlen=10):
    lines = read_lines(FILENAME)
    idx2ch, ch2idx = index_(lines)
    X, Y = to_array(lines, seqlen, ch2idx)
    return X, Y, idx2ch, ch2idx