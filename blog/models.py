from django.db import models

# Create your models here.
class Modalidade(models.Model):
    nome = models.CharField(max_length =150)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    telefone = models.CharField(max_length=150)
    data_nacimento = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length =150)
    quantidade = models.IntegerField()
    descricao = models.TextField(max_length=300)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    Alunos = models.ManyToManyField(Aluno)

    def __str__(self):
        return self.nome

