import xml.etree.ElementTree as ET

tree = ET.parse('ontology.xml')
root = tree.getroot()
print (root)

d = {}

for Disorder in root.iter('Disorder'):
    disorderName = (Disorder.find('Name')).text
    d[disorderName] = {}

    for DisorderAssociation in Disorder.iter('HPODisorderAssociation'):
        HPO = DisorderAssociation.find('HPO')
        #print (HPO.find('HPOId').text)
        HPOId = HPO.find('HPOId').text


        Freq = DisorderAssociation.find('HPOFrequency')
        #print (Freq.find('Name').text)
        Freq = Freq.find('Name').text

        d[disorderName][HPOId]  = Freq

def get_disorder_oncology_dict():
    return d
