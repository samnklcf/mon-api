from django.db import models

class tache(models.Model):
    title = models.CharField(max_length=50)
    statut = models.CharField(max_length=50)


    def __str__(self):
        return self.title

