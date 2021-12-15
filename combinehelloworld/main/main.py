import sys
import os


sys.path.insert(0,"./direA")
sys.path.insert(0,"./dirB")
from hello import hello
from world import worlds

    
print(hello(),worlds())