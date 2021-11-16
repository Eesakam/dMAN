from django.db import models

# Create your models here.
class Leads(models.Model):
    client_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    ID_num = models.CharField(max_length=13,default=0)
    alt_num = models.CharField(max_length=13)
    BB_num = models.CharField(max_length=13)

    def __str__(self):
        return self.client_name + " " + self.surname
