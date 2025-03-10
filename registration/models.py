from django.db import models

# Create your models here.
class Course(models.Model):
    code=models.CharField(max_length=4, primary_key = True)
    description = models.TextField()

class Mentor(models.Model):
    mentorid = models.CharField(max_length=4, primary_key= True)
    mentorname = models.TextField()

class Student(models.Model):
    id = models.CharField(max_length = 12, primary_key = True)
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 12)
    course_code = models.ForeignKey(Course, on_delete = models.CASCADE)

class StudentMentor(models.Model):
    studmenid = models.CharField (max_length = 12, primary_key= True)
    studid = models.ForeignKey(Student, on_delete = models.CASCADE)
    mentcode = models.ForeignKey(Mentor, on_delete = models.CASCADE)