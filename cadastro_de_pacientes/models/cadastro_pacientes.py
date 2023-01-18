from django.db import models

class Cadastro_de_paciente(models.Model):
    '''nome_paciente, sobrenome_paciente, telefone, primeiro_atendimento, email, sexo, foto, nome_completo'''
    nome_paciente = models.CharField(max_length=200)
    sobrenome_paciente = models.CharField(max_length=200)
    telefone = models.CharField(max_length=11)
    primeiro_atendimento = models.DateField()
    email = models.EmailField(max_length=200, blank=True)
    sexo_op = [
        ('M' , 'Masculino'),
        ('F' , 'Feminino'),
        ]
    sexo = models.CharField(max_length = 1, choices = sexo_op, default=0) 
    

    def __str__(self):
        return self.nome_paciente