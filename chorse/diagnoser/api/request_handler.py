

def get_symptom_by_id(id):
    return {'def': '"With the eyes in primary position, the sclera is visible above the superior corneal limbus." [https://www.aao.org/bcscsnippetdetail.aspx?id=03ad3eb3-3445-4be2-9470-2c4845169b75, PMID:8719687]', 'property_value': ['http://purl.org/dc/elements/1.1/date 2018-02-05T16:22:49Z xsd:dateTime'], 'name': 'Eyelid retraction', 'is_a': ['HP:0000492'], 'created_by': 'ORCID:0000-0001-7941-2961'}

def get_question_text():
    return ''

def get_symptoms_text(symptom_ids):
    
    for id in symptom_ids:

    return ''

def get_results_text():
    return ''

def handle_params(params=''):
    if params['symptoms']== '':
        return {
            question='',
            symptoms='This is where the symptoms you noted will appear',
            results='This is where the possible rare illness will appear'
        }
    symptom_ids = params['symptoms'].split(',')

    question_text = get_question_text(symptom_ids)
    symptoms_text = get_symptoms_text(symptom_ids)
    results_text = get_results_text(symptom_ids)
    return {'question':question_text,'symptoms': symptoms_text,'results':results_text}
