from django.db import models


# Create your models here.

# TODO add help text
class Intents(models.Model):
    id_intent = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, unique=True)
    description = models.CharField(max_length=200, null=False)
    answer = models.CharField(max_length=400, blank=True, null=False)

    # next = models.ForeignKey(BotQuestions, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'intents'
        verbose_name = "Intent"
        verbose_name_plural = "Intents"
        db_table = 'intents'

    def __str__(self):
        return self.name


# TODO fix typping
class Questions(models.Model):
    id_questions = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200, null=False, unique=True)
    intent = models.ForeignKey(Intents, on_delete=models.CASCADE, null=False)

    class Meta:
        default_related_name = 'questions'
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        db_table = 'questions'

    def __str__(self):
        return self.question


class Entities(models.Model):
    VALUE = 'V'
    REGEX = 'R'
    ENTITIES_CHOICES = (
        (REGEX, 'Regex'),
        (VALUE, 'Value')
    )
    id_entity = models.AutoField(primary_key=True)
    entity = models.CharField(max_length=100, null=False, unique=True)
    type = models.CharField(
        max_length=2,
        choices=ENTITIES_CHOICES,
        default=VALUE
    )
    synonyms = models.BooleanField(default=True)
    extensible = models.BooleanField(default=False)

    class Meta:
        default_related_name = 'entities'
        verbose_name = "Entity"
        verbose_name_plural = "Entities"
        db_table = 'entities'

    def __str__(self):
        return self.entity


class Values(models.Model):
    id_value = models.AutoField(primary_key=True)
    value = models.CharField(max_length=100, null=False)
    entity = models.ForeignKey(Entities, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'values'
        verbose_name = "Value"
        verbose_name_plural = "Values"
        db_table = 'values'

    def __str__(self):
        return self.value


class Synonyms(models.Model):
    id_synonym = models.AutoField(primary_key=True)
    synonym = models.CharField(max_length=100, null=False)

    value = models.ForeignKey(Values, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'synonyms'
        verbose_name = "Synonym"
        verbose_name_plural = "Synonyms"
        db_table = 'synonyms'

    def __str__(self):
        return self.synonym


class Slots(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    id_slot = models.AutoField(primary_key=True)
    b_index = models.IntegerField(null=False)
    e_index = models.IntegerField(null=False)
    entity = models.ForeignKey(Entities, on_delete=models.CASCADE)
    slot_name = models.CharField(max_length=60, null=False)

    class Meta:
        default_related_name = 'slots'
        verbose_name = "Slot"
        verbose_name_plural = "Slots"
        db_table = 'slots'

    def __str__(self):
        return self.slot_name

# class BotQuestions(models.Model):
#     id_bot_questions = models.AutoField(primary_key=True)
#     bot_question = models.CharField(max_length=200, null=False)
#     expected_question = models.ForeignKey(Intents, on_delete=models.CASCADE)
#     expected_entity = models.ForeignKey(Entities, on_delete=models.CASCADE)
#
#     class Meta:
#         default_related_name = 'bot_questions'
#         verbose_name = "BotQuestion"
#         verbose_name_plural = "BotQuestions"
#         db_table = 'bot_questions'
#
#     def __str__(self):
#         return self.bot_question[0:20]
