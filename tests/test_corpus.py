import sys
sys.path.append('../')

from corpora.preprocessing import Preprocessing

x = Preprocessing('crime1')
print(x.preprocessing())