import json
import networkx
import obonet

 # Read the ontology
url = 'https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.obo'
graph = obonet.read_obo(url)

# Mapping from term ID to name
id_to_name = {id_: data.get('name') for id_, data in graph.nodes(data=True)}
# Mapping from term ID to def
id_to_def = {id_: data.get('def') for id_, data in graph.nodes(data=True)}

def get_name_from_id(id):
    return id_to_name[id]

def get_def_from_id(id):
    return id_to_def[id]

def get_symptom_by_id(id):
    return graph._node[id]

def get_successors(id):
    succs = graph._succ[id]
    result = []
    for x in succs:
        result.append(x)
<<<<<<< HEAD
    return (result)

def reverse_graph():
    return graph.reverse

def remove_node(id):
    graph.remove_node(id)

# Categories for the first 25 questions / checkmarks
categories = {
    "cat1": {
        "Id" : "HP:0001871",
        "Name" : "Abnormality of blood and blood-forming tissues",
        "Def" : "Abnormality of organs that are involved in the production of blood, primarily the bone marrow, spleen, tonsils, and lymph nodes." }
    "cat2": {
        "Id" : "HP:0003549",
        "Name" : "Abnormality of connective tissue",
        "Def" : "Any abnormality of the soft tissues, including both connective tissue (tendons, ligaments, fascia, fibrous tissues, and fat)" }
    "cat3": {
        "Id" : "HP:0000152",
        "Name" : "Abnormality of head or neck",
        "Def" : "An abnormality of head and neck" }
    "cat4": {
        "Id" : "HP:0040064",
        "Name" : "Abnormality of limbs",
        "Def" : "Dysmelia, limb anomaly" }
    "cat5": {
        "Id" : "HP:0001939",
        "Name" : "Abnormality of metabolism/homeostasis",
        "Def" : "Metabolism abnormality" }
    "cat6":

    
}

def main():
    remove_node('HP:0000014')
    print (get_successors('HP:0000009'))

if __name__== "__main__":
  main()
=======
    return result
>>>>>>> e32e8f70500dfbbadfb8baedd8018d3b74b1d976
