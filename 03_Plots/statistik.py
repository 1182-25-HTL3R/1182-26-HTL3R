__author__ = "Fabian Ha"

import subprocess

subpro = subprocess.Popen(['/usr/bin/git', 'log', '--author', 'Fabian Ha'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = subpro.communicate()

if stderr:
    print(stderr)
    exit()

print(stdout)