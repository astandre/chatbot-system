from .models import *


# Todo handle bigger files
def handle_data(file, option):
    print("type ", file.content_type)
    print("size ", file.size)
    if file.content_type == "application/vnd.ms-excel":
        if option == '0':
            print("Entities")
            for chunk in file.chunks():
                values = chunk.decode("utf-8")
                values_lines = values.splitlines()
                for value_line in values_lines:
                    if value_line[len(value_line) - 1:len(value_line)] == ",":
                        values_sep = value_line[0:len(value_line) - 1].split(',')
                    else:
                        values_sep = value_line.split(',')
                    current_entity = values_sep[0]
                    current_value = values_sep[1]
                    try:
                        id_entity = Entities.objects.values('id_entity').get(entity=current_entity)
                    except Entities.DoesNotExist:
                        print(current_entity, " (entity) isn't in the database yet.")
                        print("Adding (entity) ", current_entity, " to DB")
                        entity = Entities(entity=current_entity)
                        entity.save()
                    else:
                        print(current_entity, " (entity) is in the database.")
                    finally:
                        id_entity = Entities.objects.values('id_entity').get(entity=current_entity)
                    #     Trying to store values
                    try:
                        id_value = Values.objects.values('id_value').get(value=current_value)
                    except Values.DoesNotExist:
                        print(current_value, " (value) isn't in the database yet.")
                        print("Adding (value) ", current_value, " to DB")
                        value = Values(value=current_value, entity_id=id_entity['id_entity'])
                        value.save()
                    else:
                        print(current_value, " (value) is in the database.")
                    finally:
                        id_value = Values.objects.values('id_value').get(value=current_value)
                    if len(values_sep) > 2:
                        for i in range(2, len(values_sep)):
                            current_synonym = values_sep[i]
                            try:
                                Synonyms.objects.get(synonym=current_synonym)
                            except Synonyms.DoesNotExist:
                                print(current_synonym, " (synonym) isn't in the database yet.")
                                print("Adding (synonym) ", current_synonym, " to DB")
                                synonym = Synonyms(synonym=current_synonym, value_id=id_value['id_value'])
                                synonym.save()
                            else:
                                print(current_synonym, " (synonym) is in the database.")
                                print(id_value)
                    print(values_sep)
        elif option == '1':
            print("Intents")
            for chunk in file.chunks():
                values = chunk.decode("utf-8")
                values_lines = values.splitlines()
                for value_line in values_lines:
                    if value_line[len(value_line) - 1:len(value_line)] == ",":
                        values_sep = value_line[0:len(value_line) - 1].split(',')
                    else:
                        values_sep = value_line.split(',')
                    # print(values_sep)
                    current_intent = values_sep[0]
                    print("(intent) ", current_intent)
                    # Trying to add intent
                    try:
                        id_intent = Intents.objects.values('id_intent').get(name=current_intent)
                    except Intents.DoesNotExist:
                        print(current_intent, " (intent) isn't in the database yet.")
                        print("Adding (intent): ", current_intent, " to DB")
                        intent = Intents(name=current_intent)
                        intent.save()
                    else:
                        print(current_intent, " (intent) is in the database.")
                    finally:
                        id_intent = Intents.objects.values('id_intent').get(name=current_intent)
                    # Selecting current question and slots
                    aux = ("[", "]", ":", "(", ")")
                    current_question = values_sep[1]
                    entity_b = 0
                    entity_e = 0
                    slot_b = 0
                    slot_e = 0
                    entity_name = ""
                    slot_name = ""
                    slot = False
                    for i in range(0, len(current_question)):
                        if current_question[i] == "[":
                            entity_b = i + 1
                        if current_question[i] == "]":
                            entity_e = i
                        if current_question[i] == "(":
                            slot_b = i + 1
                        if current_question[i] == ")":
                            slot_e = i
                    fix_sum = (entity_e - entity_b) + 3
                    if entity_b != 0 and entity_e != 0:
                        slot = True
                    if slot:
                        slot_aux = current_question[entity_b:entity_e].split(':')
                        slot_name = slot_aux[0]
                        entity_name = slot_aux[1]
                    #   TODO support " "
                    # if current_question[entity_e + 1] == " ":
                    #     fix_sum = fix_sum + 1
                    #     current_question = current_question[0:entity_e] + current_question[
                    #                                                     entity_e + 1:len(current_question)]
                    # if current_question[0] == " ":
                    #     current_question = current_question[1:len(current_question)]
                    #     entity_b -= 1
                    current_question = current_question[0:entity_b] + current_question[
                                                                      entity_e:len(current_question)]
                    for i in aux:
                        current_question = current_question.replace(i, "")
                    print("(question) ", current_question)
                    # Trying to a add question with slot
                    try:
                        id_question = Questions.objects.values('id_questions').get(question=current_question)
                    except Questions.DoesNotExist:
                        print(current_question, " (question) isn't in the database yet.")
                        print("Adding (question): ", current_question, " to DB")
                        question = Questions(question=current_question, intent_id=id_intent['id_intent'])
                        question.save()
                    else:
                        print(current_question, " (question) is in the database.")
                    finally:
                        id_question = Questions.objects.values('id_questions').get(question=current_question)
                        # Trying to add slots
                    print("(entity) ", entity_name)
                    if len(entity_name) > 0:
                        try:
                            id_entity = Entities.objects.values('id_entity').get(entity=entity_name)
                            slot = Slots(b_index=slot_b - fix_sum, e_index=slot_e - fix_sum, slot_name=slot_name,
                                         question_id=id_question['id_questions'], entity_id=id_entity['id_entity'])
                            slot.save()
                        except Entities.DoesNotExist:
                            print("(entity) doesnt exist")
        return True
    else:
        return False
