from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Customer_Info(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    balance = models.FloatField()
    people = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bank-customer_page', kwargs={'pk': self.pk})

'''class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="name", null=True)  # <--- added
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name'''

