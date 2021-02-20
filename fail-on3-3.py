import os, sys

print(os.environ.get('BUILD_ID'))
if (int(os.environ.get('BUILD_ID')) % 3) != 0:
    print("Fail!!!")
    sys.exit(1)
else:
    print("pass!!!")
sys.exit(0)