from django import forms

class CalculatorForm(forms.Form):
    CHOICES = [
        ('j', 'Addition'),
        ('z', 'Multiple'),
        ('t', 'Division'),
        ('m', 'Minus')
    ]
    number1 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label="first number")
    number2 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label="second number")
    operation = forms.ChoiceField(label="operation",
        widget=forms.RadioSelect,
        choices=CHOICES, 
    )
    