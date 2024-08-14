from django.db import models

from django.contrib.auth.models import User


# Create your models here.



class applicant(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE,related_name='applicant')
    gender=models.CharField(max_length=200)
    dob=models.DateField(null=True, blank=True)
    phone_number=models.IntegerField()
    marital_status=models.CharField(max_length=100,null=True)
    home_town=models.CharField(max_length=200,null=False)
    current_location=models.CharField(max_length=200,null=False)
    pincode=models.IntegerField()
    curent_locations=models.CharField(max_length=100)
    resume=models.ImageField(upload_to='resume/',blank=True,null=True)
    preferred_job_type=models.CharField(max_length=200)
    total_years_of_experince=models.IntegerField()
    availability_to_join=models.CharField(max_length=200,null=True)
    work_parmit_for_USA=models.BooleanField()
    language=models.CharField(max_length=200)
    about=models.CharField(max_length=400,default=True,null=True)



class Skill (models.Model):
    name=models.CharField(max_length=100)
    applicant_ids=models.ManyToManyField(applicant,related_name='skills')
    
