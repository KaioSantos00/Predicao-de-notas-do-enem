from django.forms import ModelForm
from .models import *

class EnemForm(ModelForm):
    class Meta:
        model = EnemScore
        fields = '__all__'