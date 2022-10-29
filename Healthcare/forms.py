from django import forms
from .models import Service

class DateInput(forms.DateInput):
    input_type = 'date'

class Form(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['disease', 'appointment_date', 'phone_number']
        disease = forms.Textarea()
        appointment_date = forms.DateField(widget=DateInput)
        phone_number = forms.CharField(max_length=50, required=True)

        labels = {
            'disease': 'Isi Penyakit Yang Terjangkit',
            'appointment_date': 'Tanggal Konsultasi',
            'phone_number': 'Isi Nomor Telepon',
        }
        
        widgets = {
            'disease': forms.Textarea(attrs={'class': 'bg-white rounded-xl p-4', 'placeholder': 'Isi Penyakit Yang Terjangkit'}),
        }
        error_messages = {
            'required' : 'Isian tidak boleh kosong',
        }