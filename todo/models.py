from django.db import models
from django.utils.timezone import now

# Create your models here.
class Todo(models.Model):
    primary_key=True
    task = models.CharField(max_length=160)
    progress = models.IntegerField()
    deadline_date = models.DateField(verbose_name='Deadline date', default=None, blank=True, null=True)
    created_date = models.DateTimeField(verbose_name='Creation date', default=now)

    def has_deadline(self):
        return self.deadline_date is None