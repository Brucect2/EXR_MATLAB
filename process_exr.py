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
img[:, :, 0] = m_file.get('Forward')[:, :, 0]
names += ['Forward']
idx = 1
for i in range(len(channels)):
    if channels[i] != 'Forward':
        img[:, :, idx] = m_file.get(channels[i])[:, :, 0]
        names += [channels[i]]
        idx += 1

io.savemat(tmp_fn, {'img':img, 'channels':names})
