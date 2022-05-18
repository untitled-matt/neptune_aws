from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
#from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

graph = Graph()

class NeptuneConnect:
    
    remoteConn = False
    endPoint = 'wss://test-graph-cluster.c8anryrp4ycm.us-east-1.neptune.amazonaws.com::8182'

    def neptune_connect(self):
        self.remoteConn = DriverRemoteConnection(self.endPoint,'g')
        #gts = traversal().withRemote(self.remoteConn)
        #return (gts, self.remoteConn)
        return graph.traversal().withRemote(self.remoteConn)

    def neptune_close_connect(self):
        self.remoteConn.close()