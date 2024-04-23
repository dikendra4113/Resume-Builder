from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Student(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Full Name", max_length=200)
    dob = models.CharField(verbose_name="Date Of Birth", max_length=200)
    email_id = models.EmailField(verbose_name="Email ID", max_length=200)
    mobile_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")],max_length=20, null = True)
#     mobile_no = models.PositiveIntegerField(verbose_name="Mobile Number")
    address = models.TextField(verbose_name="Address")
    objective = models.TextField(verbose_name="Objective")
    brief_overview = models.TextField(verbose_name="Brief Overview")
    tenth_marks = models.PositiveIntegerField(verbose_name="10 Marks")
    twe_marks = models.PositiveIntegerField(verbose_name="12 Marks")
    gradu_agg = models.PositiveIntegerField(verbose_name="Graduation Aggregate Marks")
    tech_certi = models.TextField(verbose_name="Technical Certifications")
    extra_curri = models.TextField("Extra Curricular Activities")
    project = models.TextField("Projects Made")

    def __str__(self):
        return self.name

class Template(models.Model):
    tname = models.CharField(max_length=40)
    image=models.ImageField(upload_to = "images\\", null=True)
    def __str__(self):
        return self.tname

    