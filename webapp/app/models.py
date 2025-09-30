from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=12)
    institution = models.TextField()
    department = models.TextField()
    utrNo = models.CharField(max_length=20)
    paymentSS = models.URLField()
    amount = models.IntegerField()
    isPosterPresentation=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.contact}"