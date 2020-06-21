from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)   #modelos.ForeignKey, este es una relación (link) con otro modelo
    title = models.CharField(max_length=200)                            #models.CharField, así es como defines un texto con un número limitado de caracteres
    text = models.TextField()                                           #models.TextField, este es para texto largo sin límite
    created_date = models.DateTimeField(                                #models.DateTimeField, este es fecha y hora.
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title