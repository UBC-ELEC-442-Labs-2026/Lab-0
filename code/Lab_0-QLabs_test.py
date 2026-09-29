
import os
import sys
import time
import numpy as np

import constants
from pal.products.qarm import QArm

directory_path = os.path.dirname(constants.path_to_interface)
if directory_path not in sys.path:
    sys.path.append(directory_path)

from QArm_functions import QArm_Lab_interface 


QArm_Interface = QArm_Lab_interface()
start_phi = np.array([1.0, 1.0, -1.0, 1.0])
end_phi = np.array([-1.0, 0.0, 0.0, 0.0])


with QArm(hardware=0, readMode=0) as myArm:
    QArm_Interface.attach_QArm(myArm)

    for i in range(10):
        QArm_Interface.write_to_arm(start_phi)
        time.sleep(3)
        QArm_Interface.write_to_arm(end_phi)
        time.sleep(3)
    