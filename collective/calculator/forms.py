from django.forms import ModelForm
from .models import calculator


class calculatorForm(ModelForm):
    class Meta:
        model = calculator
        fields = '__all__'