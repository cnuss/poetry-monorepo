import numpy as np

def domath():
    from libaws import whoami

    whoami.whoami()

    x = np.arange(15, dtype=np.int64).reshape(3, 5)
