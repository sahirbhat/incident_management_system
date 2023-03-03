from django.db import models
from django.utils.crypto import get_random_string
import datetime
import random
import string

class incidents(models.Model):

    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('progress', 'In Progress'),
        ('closed', 'Closed'),
    ]

    def get_random_string(length):
        
        letters = string.digits
        return ''.join(random.choice(letters) for i in range(length))
    
    id=models.IntegerField(auto_created=True,primary_key=True ,default=None,editable=False)
    incident_id = models.CharField(unique=True,max_length=15, editable=False, default='RMG' + str(datetime.date.today().year) + get_random_string(length=5))
    
    reporter_name = models.CharField( max_length=60,)
    incident_details=models.TextField(blank=False,editable=True)
    reported_date_time = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    incident_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    


    """if u wnat no incident should not be  created with close then un commit these lines of code """

    # def save(self, *args, **kwargs):
    #     if self.incident_status == 'closed' and not self.id:
    #         raise Exception('Cannot create a closed incident')
    #     elif self.incident_status == 'closed' and self.pk:
    #         raise Exception('Cannot update a closed incident')
    #     super().save(*args, **kwargs)


    def create(self, validated_data):
        validated_data['reporter_name'] = self.context['request'].user.username
        return super().create(validated_data)
    # def __str__(self):
    #     return self.incident_id




