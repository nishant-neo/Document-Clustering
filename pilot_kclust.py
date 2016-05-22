import clusters
from numpy import zeros, dot, add
#from operator import add

def printwords(list, data, words):
    vecsum = zeros(len(data[0]))
    for l in list:
        vecsum = add(data[l],vecsum)

    topwrds =  sorted(range(len(vecsum)), key=lambda x: vecsum[x])[-5:]
    for r in topwrds:
        print vecsum[r]
    print "The top words of this cluster are: \n"
    for r in topwrds:
        print words[r]


	
moviename, words, data =  clusters.readfile('res/blogdata2.txt')
print 'Processing......'
kclust = clusters.kcluster( data, k = 5)

print "\t\t******* CLUSTER 1 *******"
printwords( kclust[0], data, words)
print '\n'
print [moviename[r] for r in kclust[0]]
print '\n\n\n'


print "\t\t******* CLUSTER 2 *******"
printwords( kclust[1], data, words)
print '\n'
print [moviename[r] for r in kclust[1]]
print '\n\n\n'


print "\t\t******* CLUSTER 3 *******"
printwords( kclust[2], data, words)
print '\n'
print [moviename[r] for r in kclust[2]]
print '\n\n\n'


print "\t\t******* CLUSTER 4 *******"
printwords( kclust[3], data, words)
print '\n'
print [moviename[r] for r in kclust[3]]
print '\n\n\n'


print "\t\t******* CLUSTER 5 *******"
printwords( kclust[4], data, words)
print '\n'
print [moviename[r] for r in kclust[4]]
print '\n\n\n'


x = input(" Press any key to exit")

