# OBO Parser
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

def main():    
    

if __name__== "__main__":
  main()