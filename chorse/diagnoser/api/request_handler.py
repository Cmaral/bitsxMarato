
from diagnoser.data.ontology_data import get_symptom_by_id




#def get_symptom_by_id(id):
#    return {'def': '"With the eyes in primary position, the sclera is visible above the superior corneal limbus." [https://www.aao.org/bcscsnippetdetail.aspx?id=03ad3eb3-3445-4be2-9470-2c4845169b75, PMID:8719687]', 'property_value': ['http://purl.org/dc/elements/1.1/date 2018-02-05T16:22:49Z xsd:dateTime'], 'name': 'Eyelid retraction', 'is_a': ['HP:0000492'], 'created_by': 'ORCID:0000-0001-7941-2961'}

def get_question(ids):
    return {}

def get_symptoms(symptom_ids):
    symptoms= []
    for id in symptom_ids:
        cur_symptom = get_symptom_by_id(id)
        id2id_name = lambda x : {'symptom_id':x , 'name':get_symptom_by_id(x)['name']}
        symptoms.append({
            'symptom_id': id,
            'def':cur_symptom['def'],
            'name':cur_symptom['name'],
            'synonyms':cur_symptom['synonym'],
            'similar_symptoms':list(map(id2id_name,cur_symptom['is_a']))
        })
    return symptoms

def get_results(ids):
    return {}

def handle_params(params=''):
    if params['symptoms']== '':
        return {
            question:{'symptom_id':'HP:0000256','def':'sample_text','name':'sample_text','synonyms':[],similar_symptoms:[]},
            symptoms:[{'symptom_id':'HP:0000256','def':'sample_text','name':'sample_text','synonyms':[],similar_symptoms:[]}],
            results:{'symptom_id':'HP:0000256','def':'sample_text','name':'sample_text','synonyms':[],similar_symptoms:[]}
        }
    symptom_ids = params['symptoms'].split(',')
    question = get_question(symptom_ids)
    symptoms = get_symptoms(symptom_ids)
    results = get_results(symptom_ids)
    return {'question':question,'symptoms': symptoms,'results':results}


handle_params({'symptoms':'HP:0000256'})
