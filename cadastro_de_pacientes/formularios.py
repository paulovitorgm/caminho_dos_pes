from django import forms
from . models.cadastro_pacientes import Cadastro_de_paciente as Cadastro
from . models import anamnese

class Cadastro_de_paciente(forms.ModelForm):
    nome_paciente = forms.CharField(label='Nome do paciente', max_length=200, widget=forms.TextInput(attrs={'placeholder':'Ex: Paulo'}))
    sobrenome_paciente = forms.CharField(label='Nome do paciente', max_length=200, widget=forms.TextInput(attrs={'placeholder':'Ex: da Silva'}))
    telefone = forms.CharField(label='Telefone', max_length=11, widget=forms.TextInput(attrs={'placeholder':'(XX) XXXXX-XXXX'}))
    primeiro_atendimento = forms.DateField(label='Data do primeiro atendimento', required=False, widget=forms.DateInput(attrs={'type':'date'}),)
    email = forms.EmailField(label='Email', max_length=150, required=False ,widget=forms.EmailInput(attrs={'placeholder':'email@email.com'}))
    sexo_op = [('M' , 'Masculino'),('F' , 'Feminino')]
    sexo = forms.ChoiceField(label='Sexo', choices=sexo_op)
    
    
    class Meta:
        model = Cadastro
        exclude = ['']
       
        


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









