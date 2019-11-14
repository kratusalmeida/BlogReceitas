from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=20, null=False, blank=False)
    descricao = models.TextField()
    autor = models.CharField(max_length=20, null=False, blank=False)
    data_publicao = models.DateTimeField(auto_now_add = True)
