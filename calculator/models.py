from django.db import models

class Materials(models.Model):

    title = models.CharField(max_length=200)
    hours = models.IntegerField()

    def __str__(self):
        return self.title + '  ' + str(self.hours)
