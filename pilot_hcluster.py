import clusters
import Image
moviename, words, data =  clusters.readfile('res/blogdata2.txt')
print 'Processing......'
clust = clusters.hcluster( data)
print 'Output image is generating...'
clusters.drawdendrogram(clust, moviename, jpeg = 'output/finaloutput.jpg')
print "Scaling down..."
coords = clusters.scaledown(data)
clusters.draw2d(coords, moviename, jpeg = 'output/finaloutput2d.jpg')
image = Image.open('output/finaloutput.jpg')
image.show()
x = input("Press any key to quit....")