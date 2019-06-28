import numpy as np
import scipy.io as io
import sys


fn = sys.argv[1]
tmp_fn = sys.argv[2]

m_file = np.load(fn)

io.savemat(tmp_fn, {'out':m_file})
