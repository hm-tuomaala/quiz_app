from django.db import models

class Keys(models.Model):
    key = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=100)
    used = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    submitted = models.BooleanField(default=False)

    def __str__(self):
        return "key:" + self.key + ", used:" + str(self.used) + ", submitted:" + str(self.submitted)
