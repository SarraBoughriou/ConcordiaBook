from django.db import models

# Create your models here.
class Textbook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    edition = models.CharField(max_length=100, null=True, blank=True)
    condition_choices= [
        ('new', 'New'),
        ('written', 'Written'),
        ('old','Old')
    ]
    condition = models.CharField(max_length=20, choices=condition_choices)
    course_code = models.CharField(max_length=10)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.course_code})"