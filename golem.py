import matplotlib.pyplot as plt
from numpy import loadtxt
from urllib import urlopen

# set up path to data
baseURL = "http://golem.fjfi.cvutz.cz/utils/data/"
ShotNo = 23159
identifier = "loop_voltage"
dataURL = urlopen(baseURL + str(ShotNo) + '/' + identifier)

#load data from GOLEM server
data = loadtxt(dataURL, delimiter = '\t')

#plot graph
plt.figure()
plt.plot(data[:, 0], data[:, 1], 'k-')
plt.savefig('graph.jpg')
plt.show()

