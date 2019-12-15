
from diagnoser.data.ontology_data import get_symptom_by_id
from diagnoser.data.HPO_data import get_disorder_oncology_dict




#def get_symptom_by_id(id):
#    return {'def': '"With the eyes in primary position, the sclera is visible above the superior corneal limbus." [https://www.aao.org/bcscsnippetdetail.aspx?id=03ad3eb3-3445-4be2-9470-2c4845169b75, PMID:8719687]', 'property_value': ['http://purl.org/dc/elements/1.1/date 2018-02-05T16:22:49Z xsd:dateTime'], 'name': 'Eyelid retraction', 'is_a': ['HP:0000492'], 'created_by': 'ORCID:0000-0001-7941-2961'}

frequency_score ={
    'Very rare (<4-1%)':2,
    'Occasional (29-5%)':18,
    'Frequent (79-30%)':55,
    'Very frequent (99-80%)':90,
    'Obligate (100%)':100
}

def get_question(symptoms):

    return {}

def get_symptoms(symptoms):
    symptoms_answer = []
    print(f"symptoms :{symptoms}")
    id2id_name = lambda x : {'symptom_id':x , 'name':get_symptom_by_id(x)['name']}
    for symptom in symptoms:
        print(f"symptom :{symptom}")
        symptoms_answer.append({
            'symptom_id': id,
            'def':symptom['def'],
            'name':symptom['name'],
            'synonyms':symptom['synonym'] if 'synonym' in symptom else symptom['synonyms'],
            'similar_symptoms':list(map(id2id_name,symptom['is_a'])) if 'is_a' in symptom else None
        })
    return symptoms_answer


def distance_disorder_symptoms(disorder,symptoms):
    distance = 0
    for i in symptoms:
        match = False
        for key in disorder.keys():
            if i['symptom_id'] == key:
                distance += 100 - frequency_score[disorder[key]]
                match = True
        if match == False:
            return -1
    return distance

def get_results(symptoms):
    disorders = get_disorder_oncology_dict()
    disorder_distance = []
    for key in disorders.keys():
        distance = distance_disorder_symptoms(disorders[key],symptoms)
        if distance > 0 :
            disorder_distance.append([key,distance])
    disorder_distance = sorted(disorder_distance,key=lambda x : x[1])
    results = []
    for (i,j) in disorder_distance:
        results.append([i,j,disorders[i]])
    return results

def handle_params(params=''):
    if params['symptoms']== '':
        return {
            "question":{'symptom_id':'HP:0000256','def':'sample_text','name':'sample_text','synonyms':[],"similar_symptoms":[]},
            "symptoms":[],
            "results":{}
        }
    symptom_ids = params['symptoms'].split(',')
    symptoms = []
    for id in symptom_ids:
        print(f"id {id}")
        symptoms.append(get_symptom_by_id(id))
        symptoms[-1]['symptom_id'] = id
    question = get_question(symptoms)
    symptoms_question = get_symptoms(symptoms)
    results = get_results(symptoms)
    return {'question':question,'symptoms': symptoms_question,'results':results}


#handle_params({'symptoms':'HP:0000256'})
