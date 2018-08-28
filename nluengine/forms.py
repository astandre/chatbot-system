from django import forms


class UploadFileForm(forms.Form):
    CHOICES = (('0', 'Entities'), ('1', 'Intents'),)
    field = forms.ChoiceField(choices=CHOICES)
    file = forms.FileField()
