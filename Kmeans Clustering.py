from copy import deepcopy
from random import randint
import numpy as np
import pandas as pd
import random
import warnings
from math import sqrt
import csv
from scipy.spatial.distance import cityblock
from numpy import loadtxt
warnings.filterwarnings("ignore")
np.set_printoptions(suppress=True) #3shan el result kane bytl3 feha e [3.206e+00 7.800e-02 2.324e+02 1.380e+01 0.000e+00 0.000e+00 1.700e+01]
#fa de btsheel el e

def areEqualArrays(a,b):    #de 3shan at2ked el centroids el adeema zy el gdeda wla laa
    for i in range(0,len(a)): #3shan lw zy b3d yb2a keda mafesh no2ta et7rkt mn mknha w ra7et le cluster tanya
        for j in range(0,7):
            if a[i][j] != b[i][j]:
                return 1
        return 0

def manhattan(a,b):
    sum=0
    for i in range(0,len(a)):
        sum+=abs(a[i]-b[i])
    return sum

def euclidean(a,b):
    squared=np.square(a-b)
    summed=np.sum(squared)
    squareRoot=np.sqrt(summed)
    return squareRoot

def distnce(a, b):
    if distanceIP=='e':
        return np.linalg.norm(a - b) #np.linalg.norm() function bt7seb Euclidean distance
        
    return cityblock(a,b) 
    

def kmeans(data, clustersLocations, numOfClusters):
    clusterOfEachPoint= np.zeros(len(data)) #da array be 3dd el points ely hoa 200 w mlyan be 0,
    #array clusterOfEachPointda ba7ot feeh kol point bt belong to anhy cluster msln lw el #clusters=3
    #fa kol point hkteb 3ndha 0 aw 1 aw 2 ely hoa anhy cluster bezbt btntmy leha
    
    oldClustersCentroids = np.zeros(clustersLocations.shape) #da b2a array bkhzen feeh el clusters el adema
    #3shan ab2a a7seb el distances ben el centroids el gdeda wel adema
    #l2en lw el msafa benhom 0 y3ny el error be 0, da m3nah en mafesh point et7rkt mn mknha
    continue_iterations = True 
    while continue_iterations == True:
        for i in range(len(data)): #ha3dy 3la kol point
            distances = []  # w a3mel le kol point list esmaha distances de feha el msafa ben el point w kol centroid
            for t in clustersLocations: #by7seb le kol point el msafa benha w ben kol centroid
                distances.append(distnce(data[i], t))
                
            cluster = np.argmin(distances)  #el cluster de btsawee el index bta3 a2l distance
            #lw msln a2l distance fe index 0 da m3nah en el point de btntmy le awel cluster
            #lw a2l distance fe index 1 yb2a el point de btntmy le cluster rqm 2 w hakaza
            #print(cluster)
            clusterOfEachPoint[i] = cluster    #hena b2a ha3del fe array clusters w a7ot feeh en el point de
            #btntmy le cluster 0 or 1 or 2
            
        oldClustersCentroids = deepcopy(clustersLocations) #hena han2el el clusters centroids el adema fe oldClusters
       
        #print('----------------------hena khlssttt awel iteration')
        
        all_clusters_points=[]
        all_pointsID=[]
        for z in range (0, numOfClusters): #hena b3melhom initialize be lists fadya
            all_clusters_points.append([])#3shan a3rf amlaha t7t
            all_pointsID.append([])
            
        for c in range(0, numOfClusters): #hena ha3dy 3la kol cluster lw msln #clusters be 3 fa hanmshy 0,1,2
            points = []           
            pointsID=[]
            for y in range(len(data)):  #hashof kol point btntmy le anhy cluster
                if clusterOfEachPoint[y] == c:  #lw btntmy le cluster c ha append fe el list ely esmha points el point nfsaha
                    points.append(data[y]) #fa hena ba7ott kol el no2t ely btntmy le nfs el cluster swa
                    pointsID.append(int(dataALL[y][0])) #hena ba7tfez bel ID 3shan atb3o ta7t
            clustersLocations[c] = np.mean(points, axis=0) #w aagy hena a7sb el mean bt3hom
            all_clusters_points[c]=points
            all_pointsID[c]= pointsID
    
            continue_iterations=areEqualArrays(clustersLocations, oldClustersCentroids)
            #de lw rag3et 0 m3naha en el etnen zy b3d w sa3etha hayb2a continue_iterations be false
            
            #lw el etnen arrays zy b3d yb2a keda mafeesh point n2let cluster tanya
            #da m3nah en el old wel new clusters zy b3d fa bel taly
            #lw homa zy b3d hayrg3 0 sa3etha continue iterations hatb2a false
            #w sa3etha hanw2ff
            
        #da m3nah en homa zy b3d w mafesh point et7rkt
        #lw msh be 0 m3naha en fe point et7rkt fa 3'yaret el centers
        
        
        
    return clustersLocations, all_clusters_points, all_pointsID


#########################################################################

numOfClusters = int(input ("Enter number of clusters :"))
distanceIP= input("Euclidean press e, Manhattan press m: ")

data = np.loadtxt("Power_Consumption.csv", delimiter=',', skiprows=1, usecols=range(1,8))
dataALL = np.loadtxt("Power_Consumption.csv", delimiter=',', skiprows=1, usecols=range(0,8))
#baload el data mrten 3shan fel dataALL ba7tfez bel ID bta3 el point 3shan ama aagy atb3o ta7t


print('\nThe initial centroids choosen randomly are: \n')
featuresNumber = 7
clustersLocation = []
for i in range(numOfClusters):
    randdd=random.randint(0, 199)
    clustersLocation.append(data[randdd])  #bykhtar point random tb2a centroid
    print('  ID:', randdd+1,' => ' , data[randdd], '\n')
clustersLocations= clustersLocation 
clustersLocations= np.array(clustersLocations)

data= np.nan_to_num(data, copy=False)  #de 3shan el data kan feha nan w kan bydrbb lma yeegy y7sb el mean
#fa ana khalet kol el nans be zeros 3shan el mean yb2a mzbot
    
finalClusters, pointsInClusters,pointsID = kmeans(data, clustersLocations, numOfClusters)

for i in range (0,numOfClusters):
    print('=========================================')
    print('\nCluster ', i+1 , ' centroid is: ', finalClusters[i])
    print('\nThere are ',len(pointsInClusters[i]), ' points in cluster ', i+1, ', IDs: \n')
    print(pointsID[i])
    #for j in range (0,len(pointsInClusters[i])):
        #print( 'point ID--> ',pointsID[i][j], ': ', pointsInClusters[i][j])
        #e3mly uncomment lw 3yza ttl3y el point kamla
    
        
#############################################################################
    
def get_key(val,dictt):  #btrgg3 el key bta3 value mo3yn fel dictionary bstkhdmha ta7t fel outliers
    for key, value in dictt.items():
        if len(dictt.items()) >0:
            if val == value:
                return key
 
    return "key doesn't exist"


def show_outliers(pointsOfCluster, clusterCentroid,pointsID):  #show outliers le kol cluster
    distances= []
    distances2={} 
    [distances2.setdefault(i, []) for i in range(201)]
    
    for i in range (len(pointsOfCluster)):
        distanceFromPointToCluster=distnce(pointsOfCluster[i],clusterCentroid )
        distances.append(distanceFromPointToCluster)
        #print(i,distanceFromPointToCluster)
        distances2[pointsID[i]].append(distanceFromPointToCluster) #pointID: distance to centroid
        #3shan a3dr ageeb el pointID ta7t
    distances.sort()
    quar_5,quar_95= np.percentile(distances,[25,75])
    iqr=quar_95-quar_5
    lowerBound=quar_5-(1.5*iqr)
    upperBound=quar_95+(1.5*iqr)
    
    outliers=[]
    for i in range (len(distances)):
        
        if (distances[i]<lowerBound or distances[i]>upperBound):
        #if (distances[i]>upperBound):
            outliers.append(get_key(distances[i], distances2)) #de hatgebly el pointID ely el
            #ely el distance bt3tha akbr mn upper l2en ely a2l mn el lower msh outlier
    
    return outliers
 
 
   
   
    
for i in range (0,numOfClusters):
    print('=====================OUTLIERS==================')
    print('\nCluster ', i+1 , ' Outliers: ')
    print('Points with ID: ',show_outliers(pointsInClusters[i],finalClusters[i],pointsID[i]))
  

############################################################################ 
#lw 3yza el outliers fe kol el clustersss swa


#print('=======================================')
#print('Outliers in all data from all clusters: ')
distances=[]
distances2={}
[distances2.setdefault(i, []) for i in range(201)]

for j in range (0,numOfClusters):
    for i in range (0,len(pointsInClusters[j])):
        distanceFromPointToCluster=distnce(pointsInClusters[j][i],finalClusters[j] )
        distances.append(distanceFromPointToCluster)
        distances2[pointsID[j][i]].append(distanceFromPointToCluster)
    

distances.sort()
quar_5,quar_95= np.percentile(distances,[25,75])
iqr=quar_95-quar_5
lowerBound=quar_5-(1.5*iqr)
upperBound=quar_95+(1.5*iqr)

outliers=[]
for i in range (len(distances)):
    if (distances[i]<lowerBound or distances[i]>upperBound):
        #if (distances[i]>upperBound):
        outliers.append(get_key(distances[i], distances2))
    
#print(outliers)
#################################################################################        
    

