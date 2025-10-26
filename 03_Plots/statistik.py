__author__ = "Fabian Ha"

import subprocess

subpro = subprocess.Popen(
    ['/usr/bin/git', 'log', '--format=%an;%ad', '--author', 'Fabian Ha'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = subpro.communicate()

if stderr:
    print(stderr)
    exit()

lines = stdout.decode("utf-8").splitlines()
commits = []
for line in lines:
    print(line)
    commits.append(line)