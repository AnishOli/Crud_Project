from django.db import models
from multiselectfield import MultiSelectField

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
# Create your models here.
gender_choice=(
   ( 'male','male'),
    ('female','female'),
    ('not mentioned','not mentioned')
)
course_field=(
    ("math","math"),
    ("Science","Science"),
    ("Social","Social"),
)

class Student(models.Model):
    name= models.CharField(max_length=50,validators=[MinLengthValidator(3)])
    age=models.IntegerField()
    email = models.EmailField(unique=True)
    address = models.TextField()
    remarks= models.TextField()
    gender= models.CharField(max_length=50, choices=gender_choice )
    course= MultiSelectField(choices=course_field,max_length=200)

    def __str__(self):
        return self.name
    


class FormStudent(models.Model):
    name= models.CharField(max_length=50,validators=[MinLengthValidator(3)])
    age= models.IntegerField()
    email = models.EmailField(unique=True)
    address= models.TextField()
    message= models.TextField()
    is_delete=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    

