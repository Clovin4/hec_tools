from hms.model import Project
from hms import Hms

import glob
import sys 

hmspth = sys.argv[1]
runName = sys.argv[2]
# print 'running' + str(hmspth)


myProject = Project.open(hmspth)
myProject.computeRun(runName)
myProject.close()


Hms.shutdownEngine()