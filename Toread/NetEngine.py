import sys
sys.path.append(".")
from twisted.python import log
from twisted.internet import reactor
from ping import PingServerIF
from gossip import GossipServer
from nc import NCServer
from config import *
from Vivaldi import Vivaldi #import Vivaldi module
from Pharos import PHAROS

if LOG_IN_DETAIL>0:
    log.startLogging(sys.stdout)
#log.startLogging(open('a.out', 'W+'))

#Configure servers
PingServerIF.serv(PINGMETHOD,PINGPORT)
reactor.listenTCP(GOSSIPPORT,GossipServer.GossipServerFactory())
reactor.listenTCP(NCPORT,NCServer.NCServerFactory())

#set algorithm
if ALGORITHM == "Vivaldi":
    reactor.callWhenRunning(Vivaldi.start)
if ALGORITHM == "PHAROS":
    reactor.callWhenRunning(PHAROS.start)

reactor.run()

