

import sys

#print(sys.path)
for modulo in sys.path:
    print(modulo)


print()
import os
print(os.getenv('PYTHONPATH'))