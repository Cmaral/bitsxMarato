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
        "Def" : "Abnormality of organs that are involved in the production of blood, primarily the bone marrow, spleen, tonsils, and lymph nodes." },
    "cat2": {
        "Id" : "HP:0003549",
        "Name" : "Abnormality of connective tissue",
        "Def" : "Any abnormality of the soft tissues, including both connective tissue (tendons, ligaments, fascia, fibrous tissues, and fat)" },
    "cat3": {
        "Id" : "HP:0000152",
        "Name" : "Abnormality of head or neck",
        "Def" : "An abnormality of head and neck" },
    "cat4": {
        "Id" : "HP:0040064",
        "Name" : "Abnormality of limbs",
        "Def" : "Dysmelia, limb anomaly" },
    "cat5": {
        "Id" : "HP:0001939",
        "Name" : "Abnormality of metabolism/homeostasis",
        "Def" : "Metabolism abnormality" },
    "cat6": {
        "Id" : "HP:0001197",
        "Name" : "Abnormality of prenatal development or birth",
        "Def" : "An abnormality of the fetus or the birth of the fetus, excluding structural abnormalities." },
    "cat7": {
        "Id" : "HP:0001438",
        "Name" : "Abnormality of the abdomen",
        "Def" : "A structural abnormality of the abdomen ('belly'), that is, the part of the body between the pelvis and the thorax." },
    "cat8": {
        "Id" : "HP:0000769",
        "Name" : "Abnormality of the breast",
        "Def" : "Abnormality of the breast" },
    "cat9": {
        "Id" : "HP:0001626",
        "Name" : "Abnormality of the cardiovascular system",
        "Def" : "The cardiovascular system consists of the heart, vasculature, and the lymphatic system." },
    "cat10": {
        "Id" : "HP:0000598",
        "Name" : "Abnormality of the ear",
        "Def" : "Either a morphological abnormality or hearing deficit" },
    "cat11": {
        "Id" : "HP:0000818",
        "Name" : "Abnormality of the endocrine system",
        "Def" : "The endocrine system is composed of glands that secrete hormones directly into the bloodstream and includes the following glands: thyroid, parathyroids, adrenals, pancreas, gonads (testicles and ovaries), and pituitary. Many other organs, such as the kidney, liver, and heart, have secondary endocrine functions." },
    "cat12": {
        "Id" : "HP:0000478",
        "Name" : "Abnormality of the eye",
        "Def" : "ny abnormality of the eye, including location, spacing, and intraocular abnormalities" },
    "cat13": {
        "Id" : "HP:0000119",
        "Name" : "Abnormality of the genitourinary system",
        "Def" : "The presence of any abnormality of the genitourinary or urinary system." },
    "cat14": {
        "Id" : "HP:0002715",
        "Name" : "Abnormality of the immune system",
        "Def" : "The immune system is composed of organs and interdependent cell types that collectively protect the body from infections and from the growth of tumor cells. The organs of the immune system comprise the bone marrow, the spleen, the thymus,the lymph nodes, and the cell types comprise B cells, T cells, natural killer cells, granulocytes,dendritic cells, and macrophages." },
    "cat15": {
        "Id" : "HP:0001574",
        "Name" : "Abnormality of the integument",
        "Def" : "An abnormality of the integument, which consists of the skin and the superficial fascia." },
    "cat16": {
        "Id" : "HP:0003011",
        "Name" : "Abnormality of the musculature",
        "Def" : "Abnormality originating in one or more muscles, i.e., of the set of muscles of body." },
    "cat17": {
        "Id" : "HP:0000707",
        "Name" : "Abnormality of the nervous system",
        "Def" : " The nervous system comprises the neuraxis (brain, spinal cord, and ventricles), the autonomic nervous system, the enteric nervous system, and the peripheral nervous system." },
    "cat18": {
        "Id" : "HP:0002086",
        "Name" : "Abnormality of the respiratory system",
        "Def" : "An abnormality of the respiratory system, which include the airways, lungs, and the respiratory muscles" },
    "cat19": {
        "Id" : "HP:0000924",
        "Name" : "Abnormality of the skeletal system",
        "Def" : "Abnormality of the skeletal system" },
    "cat20": {
        "Id" : "HP:0045027",
        "Name" : "Abnormality of the thoracic cavity",
        "Def" : "Abnormality of the thoracic cavity" },
    "cat21": {
        "Id" : "HP:0001608",
        "Name" : "Abnormality of the voice",
        "Def" : "This term describes any abnormality of the voice, i.e., of the sounds produced by humans by the passage of air through the larynx and over the vocal cords, and then modified by the resonance organs, the nasopharynx, and the mouth." },
    "cat22": {
        "Id" : "HP:0001507",
        "Name" : "Growth abnormality",
        "Def" : "Abnormal growth" },
    "cat23": {
        "Id" : "HP:0002664",
        "Name" : "Neoplasm",
        "Def" : "An organ or organ-system abnormality that consists of uncontrolled autonomous cell-proliferation which can occur in any part of the body as a benign or malignant neoplasm (tumour)" },
}

with open('categories.json', 'w') as fp:
    json.dump(categories, fp)

def main():
    remove_node('HP:0000014')
    print (get_successors('HP:0000009'))

if __name__== "__main__":
  main()
