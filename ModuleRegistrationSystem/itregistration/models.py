from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Module(models.Model):
    moduleid = models.AutoField(primary_key=True)
    modulename= models.CharField(max_length = 100)
    category = models.CharField(max_length = 100, choices = [('Cybersecurity', 'Cybersecurity'),
                ('Data Science', 'Data Science'), 
                ('Software Development', 'Software Development'), 
                ('Web Designing', 'Web Designing'), 
                ('VFX and Animation', 'VFX and Animation'), 
                ('Games Design', 'Games Design')])
    credit = models.SmallIntegerField()
    description = models.CharField(max_length = 10000)
    available = models.BooleanField()

    def __str__(self):
        return f'Module; {self.modulename}, Module ID; {self.moduleid}.'
    
class Course(models.Model):
    coursename=models.CharField(max_length=100, default='Course Name')
    description=models.CharField(max_length=10000)
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return f'{self.coursename}'
    
class Registration(models.Model):
    student = models.ForeignKey(User, on_delete = models.CASCADE)
    module = models.ForeignKey(Module, on_delete = models.CASCADE)
    date_of_registration = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f'{self.student} registered to {self.module}'