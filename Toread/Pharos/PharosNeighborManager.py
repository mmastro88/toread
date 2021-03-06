from neighbor.NeighborManagerIF import *
from Vivaldi.VivaldiNeighborManager import *


class PharosNeighborManager(NeighborManagerIF):
    def __init__(self):
        self.globalNeighborMgr = VivaldiNeighborManager(PHAROS_USING_HEIGHT_GLOBAL, PHAROS_DIMENSION_GLOBAL, PHAROS_UPDATE_STRATEGY_GLOBAL)
        self.clusterNeighborMgr = VivaldiNeighborManager(PHAROS_USING_HEIGHT_LOCAL, PHAROS_DIMENSION_LOCAL, PHAROS_UPDATE_STRATEGY_LOCAL) 
        return 
    
    def addGlobalClient(self, client):
        self.globalNeighborMgr.addClient(client)
        return
    
    def addClusterClient(self, client):
        self.clusterNeighborMgr.addClient(client)
        return
    
    def updateGlobalNeighbor(self, neighbor):
        self.globalNeighborMgr.update( neighbor )
        return
    
    def updateClusterNeighbor(self, neighbor ):
        self.clusterNeighborMgr.update( neighbor )
        return
    
    def getClusterNeighbor( self, ip ):
        return self.clusterNeighborMgr.getNeighbor(ip)
    
    def getGlobalNeighbor(self, ip ):
        return self.globalNeighborMgr.getNeighbor(ip)
    
    def removeGlobalNeighbor(self, ip):
        r = self.globalNeighborMgr.removeIP(ip)
        return r 
    
    def removeClusterNeighbor( self, ip ):
        r = self.clusterNeighborMgr.removeIP(ip)
        return r
    
    

'''
class VivaldiNeighborManager(NeighborManagerIF):
    def __init__(self):
        self.neighborList = []
        self.updateCount = -1
        self.updateList = []
        
    def getLength(self):
        return len(self.neighborList)
    
    def add(self, client):
        tmp = VivaldiNeighbor()
        tmp.setClient(client)
        if(self.getLength() == 0):
            self.neighborList.append(tmp)
            return
        for i in xrange(self.getLength()):
            if(tmp.getIP() == self.neighborList[i].getIP()):
                if(tmp.getError() < self.neighborList[i].getError()):
                    self.neighborList[i].setClient(client)
                return
        self.neighborList.append(tmp)
    
    def update(self, neighbor):
        for i in xrange(self.getLength()):
            if(neighbor.getIP() == self.neighborList[i].getIP()):
                self.neighborList[i].update(neighbor.client.coor.getCoor(), neighbor.getError(), neighbor.getRTT())
                
    def printNeighbor(self, i):
        self.neighborList[i].printInfo()
    
    def printNeighborList(self):
        for i in xrange(self.getLength()):
            self.printNeighbor(i)
            
    def randomNC(self):
        if(self.getLength() == 0):
            self.updateCount = -1
            return
        if(self.updateCount == -1 or self.updateCount == VIVALDI_SELECTED_NEIGHBOR_NUM - 1 or self.updateCount == self.getLength() - 1):
            self.updateList = random.sample(range(0, self.getLength()), min(VIVALDI_SELECTED_NEIGHBOR_NUM, self.getLength()))
            self.updateCount = 0
        else:
            self.updateCount = self.updateCount + 1

    def closestNC(self):
        if(self.getLength() == 0):
            self.updateCount = -1
            return
        if(self.updateCount == -1 or self.updateCount == VIVALDI_SELECTED_NEIGHBOR_NUM - 1 or self.updateCount == self.getLength() - 1):
            if(self.getLength() <= VIVALDI_SELECTED_NEIGHBOR_NUM):
                self.updateList = range(self.getLength())
                self.updateCount = 0
                return
            tmpList = []
            self.updateList = []
            for i in xrange(self.getLength()):
                if(len(tmpList) == 0):
                    tmpList.append(i)
                else:
                    if(self.neighborList[i].getRTT == []):
                        tmpList.append(i)
                    else:
                        for j in xrange(i):
                            if(self.neighborList[j].getRTT() == []):
                                tmpList.insert(j, i)
                                break
                            if(self.neighborList[i].getRTT() < self.neighborList[tmpList[j]].getRTT()):
                                tmpList.insert(j, i)
                                break
                        if (j == i-1):
                            tmpList.append(i)
            for i in xrange(VIVALDI_SELECTED_NEIGHBOR_NUM):
                self.updateList.append(tmpList[i])
            self.updateCount = 0
        else:
            self.updateCount = self.updateCount + 1
        
    def hybridNC(self):
        if(self.getLength() == 0):
                self.updateCount = -1
                return
        if(self.updateCount == -1 or self.updateCount == VIVALDI_SELECTED_NEIGHBOR_NUM - 1 or self.updateCount == self.getLength() - 1):
            if(self.getLength() <= VIVALDI_SELECTED_NEIGHBOR_NUM):
                self.updateList = range(self.getLength())
                self.updateCount = 0
                return
            tmpList = []
            self.updateList = []
            for i in xrange(self.getLength()):
                if(len(tmpList) == 0):
                    tmpList.append(i)
                else:
                    if(self.neighborList[i].getRTT == []):
                        tmpList.append(i)
                    else:
                        for j in xrange(i):
                            if(self.neighborList[j].getRTT() == []):
                                tmpList.insert(j, i)
                                break
                            if(self.neighborList[i].getRTT() < self.neighborList[tmpList[j]].getRTT()):
                                tmpList.insert(j, i)
                                break
                        if (j == i-1):
                            tmpList.append(i)
            for i in xrange(VIVALDI_SELECTED_NEIGHBOR_NUM/2):
                self.updateList.append(tmpList[i])
            for i in xrange(VIVALDI_SELECTED_NEIGHBOR_NUM / 2):
                self.updateList.append(tmpList[i])
            self.updateCount = 0
        else:
            self.updateCount = self.updateCount + 1
        
    def selectIP(self):
        if (VIVALDI_UPDATE_STRATEGY == 0):
            self.randomNC()
        elif (VIVALDI_UPDATE_STRATEGY == 1):
            self.closestNC()
        elif (VIVALDI_UPDATE_STRATEGY == 2):
            self.hybridNC()
        tmp = self.updateList[self.updateCount]
        return self.neighborList[tmp].getIP()
      
    def upload(self):
        if(self.getLength() < VIVALDI_UPLOAD_NUM):
            return range(self.getLength())
        tmp = random.sample(range(self.getLength()), VIVALDI_UPLOAD_NUM)
        return tmp
    

'''
