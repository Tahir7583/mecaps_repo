from django.db import models

# Create your models here.



class applicant(models.Model):
    applicant_name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    applicant_photo=models.ImageField(upload_to='profile/',blank=True,null=True)


class Skill (models.Model):
    name=models.CharField(max_length=100)
    applicant_ids=models.ManyToManyField(applicant,related_name='skills')
    
