import subprocess as sp
import sys

command = sys.argv[1]

# output = sp.getoutput(command)
output_status = sp.getstatusoutput(command)

if output_status[0] == 0:
    print(output_status[1])
else:
    print(output_status)