from django.db import models

# Create your models here.
from django.db.models import Model


class Faculty_by_admin(Model):
    name=models.CharField(max_length=200)
    mobile_number=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    status=models.CharField(max_length=200,default="active")
    def __str__(self):
        return self.name

class Faculty(Model):
    name=models.CharField(max_length=200)
    mobile_number=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    branch = models.CharField(max_length=200,default='Computer Science')
    password=models.CharField(max_length=200)
    status=models.CharField(max_length=200,default="active")
    pic=models.ImageField(upload_to='media/image/',default='image/default/profile.jpg')
    def __str__(self):
        return self.name

class Video(Model):
    topic_name=models.CharField(max_length=200)
    subject_name=models.CharField(max_length=200)
    faculty_name=models.CharField(max_length=200)
    faculty_email=models.CharField(max_length=200)
    notes=models.FileField(upload_to='media/image/notes/',blank=True)
    video=models.FileField(upload_to='media/image/video/')
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.topic_name


class Contact(Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    message=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email