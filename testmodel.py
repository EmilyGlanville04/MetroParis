#verifico se ho costruito il grafo correttamente

from model.model import Model

model = Model()
print("Numero nodi:", model.get_numnodi())
print("Numero archi:", model.get_numarchi())
model.buildGraph()

print("Numero nodi:", model.get_numnodi())
print("Numero archi:", model.get_numarchi())
