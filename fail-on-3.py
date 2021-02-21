import os, sys

print( 'This is a build number {} of JOB: {}'.format(os.environ.get('BUILD_ID'), os.environ.get('JOB_NAME')))
if (int(os.environ.get('BUILD_ID')) % 3) != 0:
    print("Fail!!!")
    sys.exit(1)
else:
    print("pass!!!")
sys.exit(0)