library(raster)

r <- raster(nrow=18, ncol=36, xmn=0)
r[150:250] <- 1
r[251:450] <- 2
plot( boundaries(r, type='outer') )
plot( boundaries(r, classes=TRUE) )

library(jpeg)
img <- readJPEG('images/Figure-41.jpg')


library(EBImage)
img <- readImage('images/Figure-41.jpg')
colorMode(img)<-Grayscale
colorMode(img)<-Color

display(img1 <- channel(img,mode = 'green'))

x <- img1@.Data
plot(density(as.numeric(x)))
plot(r1 <- raster(x))
x[which(x>.3,arr.ind = TRUE)] <- 1
plot(density(as.numeric(x)))
r1 <- raster(x)
plot(r1)

display(img)

d <- as.matrix(read.csv('edges.csv',header=FALSE))
thresh <- .02
d[which(d<thresh,arr.ind=TRUE)] <- 0
d[which(d>=thresh,arr.ind=TRUE)] <- 1
plot(density(as.numeric(d)))
image(d,col=c('white','black','black'))

X <- which(d==1,arr.ind=TRUE)

library(fpc)

library(fastcluster)
x2 <- X[sample(1:nrow(X),10000),]
d.x <- dist(x2)
h <- hclust(d.x,method='single')

clust <- cutree(h,k =500)

#res <- dbscan(d.x,2)
#clust <- res$cluster

image(d,col=c('white','black'))
r1 <- max(X[,1])
r2 <- max(X[,2])
points(x2[,1]/r1,x2[,2]/r2,col=clust,pch=20,cex=.5)

library(vegan)
mst <- spantree(d.x)
plot(mst)

