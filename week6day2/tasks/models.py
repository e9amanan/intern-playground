# models.py
from django.db import models

class Task(models.Model):
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    
    title = models.CharField(max_length=100)
    
    
    description = models.TextField(blank=True, null=True)
    
    
    due_date = models.DateField(blank=True, null=True)
    
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    
    def __str__(self):
        return self.title