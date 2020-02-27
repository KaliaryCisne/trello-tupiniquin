from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=255)


class Description(models.Model):
    content = models.TextField()
    name = models.CharField(max_length=255, null=True)
    status = models.ForeignKey(
        'Status',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Pessoa(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)

    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf


class Usuario(Pessoa):
    email = models.CharField(max_length=255)

    def __init__(self, name, cpf, email):
        super().__init__(name, cpf)
        self.email = email
