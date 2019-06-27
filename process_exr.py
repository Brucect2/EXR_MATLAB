import numpy as np
import scipy.io as io
import sys
import pyexr

fn = sys.argv[1]
tmp_fn = sys.argv[2]

m_file = pyexr.open(fn)

channels = m_file.channels

img = np.zeros(m_file.get().shape)

names =[]

if (len(channels) == 1):
        img[:, :, 0] = m_file.get(channels[0])[:, :, 0]
        names =[channels[0]]
elif 'R' in channels:
        img[:, :, 0] = m_file.get('R')[:, :, 0]
        img[:, :, 1] = m_file.get('G')[:, :, 0]
        img[:, :, 2] = m_file.get('B')[:, :, 0]
        names += ['R', 'G', 'B']
elif 'Forward' in channels:
        img[:, :, 0] = m_file.get('Forward')[:, :, 0]
        names += ['Forward']
        idx = 1
        for i in range(len(channels)):
                if channels[i] != 'Forward':
                        img[:, :, idx] = m_file.get(channels[i])[:, :, 0]
                        names += [channels[i]]
                        idx += 1

io.savemat(tmp_fn, {'img':img, 'channels':names})
