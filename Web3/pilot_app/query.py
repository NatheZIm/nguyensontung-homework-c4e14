from mlab import mlab_connect
from models.river import *
mlab_connect()
#ex 2
# africa = River.objects(continent = "Africa")
# print(riv)
#ex 3
america = River.objects(continent = "S.America",length__lt = 1000)
print(america)
