from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMapFermate = {}
        for f in self._fermate:
            self._idMapFermate[f.id_fermata] = f


    def buildGraph(self):
        self._grafo.clear() #svuoto il mio grafo nel caso dovessi premere di nuovo il pulsante
        self._grafo.add_nodes_from(self._fermate) #la mia lista -> ciascuna fermata corrisponde a un vertice
        self.addedges3()

#doppio ciclo for: poco ottimale
    def addedges(self):
        #verifichiamo se due fermate hanno una connessione
        for u in self._fermate:
            for v in self._fermate:
                if DAO.hasconn(u,v):
                    self._grafo.add_edge(u,v)


    def addedges2(self):
        for u in self._fermate:
            for conn in DAO.getvicini(u):
                v = self._idMapFermate[conn.id_stazA]
                self._grafo.add_edge(u,v)

#PROVIAMO UN ALTRO METODO SENZA CICLI FOR
    def addedges3(self):
        alledges = DAO.getAllEdges()
        for conn in alledges:
            u =self._idMapFermate[conn.id_stazP]
            v = self._idMapFermate[conn.id_stazA]
            self._grafo.add_edge(u, v)


    def get_numnodi(self):
        return len(self._grafo.nodes())

    def get_numarchi(self):
        return len(self._grafo.edges())

    @property
    def fermate(self):
        return self._fermate