from django.db import models

# Create your models here.
class Lead(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=200, null=True)
    message = models.TextField(blank=False, null=False)
    time_received = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} working at {self.company}"
