from django.db import models


class Aluno(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    cpf = models.CharField(max_length=14, null=False, blank=False)
    nome = models.CharField(max_length=200, null=False, blank=False)
    telefone = models.CharField(max_length=14, blank=False, null=False)
    sexo = models.CharField(choices=SEXO_CHOICES,
                            max_length=1, null=False, blank=False)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome  # Retorna o nome do aluno como representação de string
    
class Professor(models.Model):
    cpf = models.CharField(max_length=14, null=False, blank=False)
    nome = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.nome  # Retorna o nome do professor como representação de string