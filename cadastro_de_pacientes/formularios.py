from django import forms
from datetime import datetime
from django.db import models
from . models import Cadastro_de_paciente
from . models import anamnese

class Cadastro_de_paciente(forms.ModelForm):
    
    class Meta:
        model = Cadastro_de_paciente
        fields = '__all__'



class Anamnese(forms.ModelForm):
    
    class Meta:
        model = anamnese.Anamnese
        
        fields = ['acompanhamento_medico', 'especialidade', 'uso_medicacao', 'medicamento_em_uso','diabetico','hepatite', 'hiv','problemas_circulatorios','alergico', 'alergia_a', 'teve_cancer', 'tipo_cancer', 'gravidez', 'lactante', 'hipertensao', 'hipotensao', 'observacoes'
        ]
        labels = {
            'acompanhamento_medico':'Acompanhamento medico',
            'especialidade':'Especialidade',
            'uso_medicacao':'Faz uso de medicacao',
            'medicamento_em_uso':'Medicamento em uso',
            'diabetico' : 'Diabético',
            'hepatite' : 'Hepatite',
            'hiv' : 'HIV',
            'problemas_circulatorios' : 'Problemas de ciculação',
            'alergico' : 'Alergico',
            'alergia_a' : 'Alergia a',
            'teve_cancer' : 'Já teve câncer',
            'tipo_cancer' : 'Tipo de câncer',
            'gravidez' : 'Gestante',
            'lactante' : 'Lactante',
            'hipertensao' : 'Tem pressão alta',
            'hipotensao' : 'Tem pressão baixa',
            'observacoes' : 'Observações'
        }









