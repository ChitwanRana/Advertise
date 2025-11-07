from django.db import models
from django.utils import timezone

class FSSAIEntry(models.Model):
    fssai_code = models.CharField(max_length=100)
    authorisation_name = models.CharField(max_length=150)
    date_of_delivery = models.DateField()
    number_of_orders = models.PositiveIntegerField()
    logo = models.ImageField(upload_to='logos/')
    certificate = models.FileField(upload_to='certificates/')
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.authorisation_name} - {self.fssai_code}"

class Review(models.Model):
    entry = models.ForeignKey(FSSAIEntry, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} ({self.rating}/5)"
