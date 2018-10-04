from snips_nlu import SnipsNLUEngine, load_resources
from .models import *
from django.db.models import Count
from .models import Intents, Questions, Entities
from snips_nlu.default_configs import CONFIG_ES
import json


# TODO multiple slots in question
# TODO check duplicated keys are being obtained in intents
def get_training_data():
    try:
        intents_list = Intents.objects.values('id_intent', 'name') \
            .annotate(num_questions=Count('questions__question'))
        entities_list = Entities.objects.values('id_entity',
                                                'entity',
                                                'synonyms',
                                                'extensible').annotate(num_values=Count('values__value'))
        intents = ''
        contador_intents = 1
        for intent_iterator in intents_list:
            # print(intent_iterator)
            question_list = Questions.objects.values('intent', 'id_questions', 'question') \
                .filter(intent_id=intent_iterator['id_intent']).annotate(num_slots=Count('slots__question'))
            questions = ''
            contador_question = 1
            for question_itearator in question_list:
                # print("     ", question_itearator)
                if question_itearator['num_slots'] > 0:
                    slots_list = Slots.objects.values('b_index',
                                                      'e_index',
                                                      'entity__entity',
                                                      'slot_name') \
                        .filter(question__id_questions=question_itearator['id_questions'])
                    question_section = ''
                    if question_itearator['num_slots'] == 1:
                        # print("         ", slots_list[0])
                        slot = '{"text":"' + question_itearator['question'][
                                             slots_list[0]['b_index']:slots_list[0]['e_index']] + '","entity":"' + \
                               slots_list[0]['entity__entity'] + '","slot_name":"' + slots_list[0]['slot_name'] + '"}'
                        if len(question_itearator['question']) == slots_list[0]['e_index']:
                            question_section += '{"data":[{"text":"' + question_itearator['question'][
                                                                       0:slots_list[0]['b_index']] + '"},'
                            question_section += slot + ']}'
                        else:
                            question_section += '{"data":[{"text":"' + question_itearator['question'][
                                                                       0:slots_list[0]['b_index']] + '"},'
                            question_section += slot + ','
                            question_section += '{"text":"' + question_itearator['question'][
                                                              slots_list[0]['e_index']:len(
                                                                  question_itearator['question'])] + '"}]}'
                        if contador_question < intent_iterator['num_questions']:
                            question_section += ','
                    else:
                        contador_slots = 1
                        # TODO support multiple entities in a question
                        for slot_iterator in slots_list:
                            # print("         ", slot_iterator)
                            slot = '{"text":"' + question_itearator['question'][
                                                 slot_iterator['b_index']:slot_iterator['e_index']] + '","entity":"' + \
                                   slot_iterator['entity__entity'] + '","slot_name":"' + slot_iterator[
                                       'slot_name'] + '"}'
                            question_section += '{"data":[{"text":"' + question_itearator['question'][
                                                                       0:slot_iterator['b_index']] + '"},'
                            question_section += slot + ','
                            question_section += '{"text":"' + question_itearator['question'][
                                                              slot_iterator['e_index']:len(
                                                                  question_itearator['question'])] + '"}'
                            question_section += ']}'
                            if contador_slots < len(slots_list):
                                question_section += ','
                            contador_slots += 1
                        if contador_question < intent_iterator['num_questions']:
                            question_section += ','
                    questions += question_section
                else:
                    if contador_question < intent_iterator['num_questions']:
                        questions += '{"data":[{"text":"' + question_itearator['question'] + '"}]},'
                    else:
                        questions += '{"data":[{"text":"' + question_itearator['question'] + '"}]}'
                intent = '"' + intent_iterator["name"] + '":{"utterances":[ ' + questions
                contador_question += 1
            if contador_intents < len(intents_list):
                intents += intent + ']},'
            else:
                intents += intent + ']}'
            contador_intents += 1

        entities = ''
        entity_contador = 1
        for entity_iterator in entities_list:
            # print(entity_iterator)
            values_list = Values.objects.values('id_value', 'entity', 'value').filter(
                entity=entity_iterator['id_entity']).annotate(num_syn=Count('synonyms__synonym'))
            entities += '"' + entity_iterator['entity'] + '":{'
            entities += '"use_synonyms":' + str(entity_iterator['synonyms']).lower() + ','
            entities += '"automatically_extensible":' + str(entity_iterator['extensible']).lower() + ','
            entities += '"data": ['
            values = ''
            value_contador = 1
            for value_iterator in values_list:
                # print("     ", value_iterator)
                value = '{"value": "' + value_iterator['value'] + '",'
                synonyms = ''
                if value_iterator['num_syn'] > 0:
                    synonyms_list = Synonyms.objects.values('id_synonym', 'value', 'synonym').filter(
                        value=value_iterator['id_value'])
                    synonyms = '"synonyms": ['
                    synonym_contador = 1
                    for synonym_iterator in synonyms_list:
                        # print("         ", synonym_iterator)
                        synonyms += '"' + synonym_iterator['synonym'] + '"'
                        if synonym_contador < value_iterator['num_syn']:
                            synonyms += ','
                        synonym_contador += 1
                    synonyms += ']'
                else:
                    value += '"synonyms": []'
                value += synonyms + '}'
                if value_contador < entity_iterator['num_values']:
                    value += ','
                value_contador += 1
                values += value
            values += ']'
            entities += values + '}'
            if entity_contador < len(entities_list):
                entities += ','
            entity_contador += 1

        full_data = '{"intents": {' + intents + '},"entities":{' + entities + '},"language": "es"}'
        return full_data
    except (
            Slots.DoesNotExist, Values.DoesNotExist, Questions.DoesNotExist, Synonyms.DoesNotExist,
            Entities.DoesNotExist,
            Intents.DoesNotExist):
        return "0"


def train_engine():
    data = get_training_data()
    print(data)
    if data != "0":
        data_json = json.loads(data)
        print("Training")
        engine.fit(data_json)
        print("Training done!")


def resolve_query(text):
    intent = engine.parse(text)
    response = {}
    print(">> (INTENT): ", intent)
    if intent['intent'] is not None:
        response["intent"] = intent['intent']['intentName']
        # response["probability"] = intent["intent"]["probability"]
        response["slots"] = intent["slots"]
    else:
        response["intent"] = None
        response["input"] = intent['input']
    return response


load_resources("snips_nlu_es")
engine = SnipsNLUEngine(config=CONFIG_ES)
# Comment this to not train engine when system is starting.
train_engine()
