import os 
import sys

if len(sys.argv) <= 1:
    exit(0)

print(os.path.getsize(sys.argv[1]))

